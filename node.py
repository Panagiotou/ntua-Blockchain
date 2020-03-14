from block import Block
from wallet import Wallet
from transaction import Transaction
import time
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from random import randint
import jsonpickle
import requests

def makeRSAjsonSendable(rsa):
    return rsa.exportKey("PEM").decode('ascii')
def makejsonSendableRSA(jsonSendable):
    return RSA.importKey(jsonSendable.encode('ascii'))

class Node:
    def __init__(self):

    	self.chain = None
    	self.current_id_count = None # +1 every time a node is added
    	self.id = None # 0...n-1
    	self.NBCs = None
    	self.wallet = None # created with create_wallet()
    	self.ring = []   #here we store information for every node, as its id, its address (ip:port) its public key and its balance
    	self.create_wallet()
    	self.previous_block = None
    	self.current_block = None
    	self.block_capacity = None


    def create_new_block(self, index, previousHash, nonce, timestamp, difficulty, capacity):
    	return Block(index, previousHash, nonce, timestamp, difficulty, capacity)

    def create_wallet(self):
    	#create a wallet for this node, with a public key and a private key
    	self.wallet = Wallet()

    def create_transaction(self, sender, sender_private_key, receiver, amount):
    	transaction = Transaction(sender, sender_private_key, receiver, amount)
    	# transaction.transaction_inputs = ...
    	self.broadcast_transaction(transaction)
    	return transaction


    def broadcast_transaction(self, transaction):
        for r in self.ring:
            baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])

            transactionjson = jsonpickle.encode(transaction)
            print("I am node with id {} and I am broadcasting the transaction ({}) to node {} with url {}".format(self.id, transaction.transaction_id_hex,  r['id'], baseurl))
            res = requests.post(baseurl + "ValidateTransaction", json = {'transaction':transactionjson})
            print(res.text)



    def validate_transaction(self, transaction):
        print("Validation I am node {} right now".format(self.id))
        for r in self.ring:
            if(r['public_key'] == transaction.sender_address):
                print("This transaction was sent to me by Node", r['id'])

        print(transaction.sender_address)
        print(transaction.receiver_address)
        print(transaction.transaction_id)


        sender_address=transaction.sender_address
        ##use temp until h is passed humanly
        h= SHA.new(transaction.transaction_myid.encode())
        signature=transaction.signature
        pubkey=sender_address
        verified = PKCS1_v1_5.new(pubkey).verify(h, signature)
        print("Verification", verified)
        if(verified):
            return True
        else:
            return False


    def add_transaction_to_block(self, transaction, block):
    	capacity = block.capacity
    	if(self.chain): # first transaction
            print("I am node with id {} and I am adding transaction ({}) to block ({})".format(self.id, transaction.transaction_id_hex, block.timestamp))
            block.add_transaction(transaction)
            #if enough transactions  mine
            print(len(block.listOfTransactions), capacity)
            if(len(block.listOfTransactions) == capacity):
            	mined_block = self.mine_block(block)
            	self.broadcast_block(mined_block)
            	# what hapens after block is mined???
            	# create new block here?
            	#TODO
    	else:
    		block.add_transaction(transaction)


    def mine_block(self, block):
        print("Mining block")
        block.nonce = 0
        while ( not (block.myHash(block.nonce).hexdigest().startswith('0'* block.difficulty))):
            block.nonce += 1
            # print(block.myHash(block.nonce).hexdigest())

        print("Block is mined.")
        return block
        #TODO run a simulation to see if all transactions can happen e.g i have 100$, give 100$ to a and give 100$ to b

    def broadcast_block(self, block):
    	for r in self.ring:
    		baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])

    		blockjson = jsonpickle.encode(block)
    		print("I am node with id {} and I am broadcasting block ({}) to {}".format(self.id, block.timestamp, baseurl))
    		res = requests.post(baseurl + "ValidateBlock", json = {'block':blockjson})
    		print(res.text)
    # def valid_proof(.., difficulty=MINING_DIFFICULTY):




    #concencus functions

    def validate_block(self, block):
    	print("I am node with id {} and I am Validating block ({})".format(self.id, block.timestamp))

    	# if(block.gethash has number of zeros...)
    	if block.previousHash == self.chain.chain[-1].currentHash:
    		# if previousHash is same as actual previous hash.
    		return True
    	else:
    		return self.resolve_conflicts(block)



    def validate_chain(self, blockchain):
    	print("Validating blockchain...")
    	for block in blockchain.chain:
    		if(block.index > 0):
    			# Block is not genesis
    			self.validate_block(block)
    	print("Blockchain Validated.")

    def resolve_conflicts(self, block):
    	#TODO resolve correct chain
    	print("Resolving")
    	return True
