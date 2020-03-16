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
from _thread import *
import threading

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
        self.myip = None
        self.myport = None

    def create_new_block(self, index, previousHash_hex, nonce, timestamp, difficulty, capacity):
    	return Block(index, previousHash_hex, nonce, timestamp, difficulty, capacity)

    def create_wallet(self):
    	#create a wallet for this node, with a public key and a private key
    	self.wallet = Wallet()

    def create_transaction(self, sender, sender_private_key, receiver, amount):
        transaction = Transaction(sender, sender_private_key, receiver, amount)
        # transaction.transaction_inputs = ...
        if(transaction.signature):
            transactionjson = jsonpickle.encode(transaction)
            baseurl = 'http://{}:{}/'.format(self.myip, self.myport)
            res = requests.post(baseurl + "ValidateTransaction", json = {'transaction':transactionjson})

        for r in self.ring:
            start_new_thread(self.broadcast_transaction, (transaction, r, ))
            # self.broadcast_transaction(transaction, baseurl)
        return transaction


    def broadcast_transaction(self, transaction, r):
        baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])
        transactionjson = jsonpickle.encode(transaction)
        print("I am node with id {} and I am broadcasting the transaction ({}) to node {} with url {}".format(self.id, transaction.transaction_id_hex,  r['id'], baseurl))

        res = requests.post(baseurl + "ValidateTransaction", json = {'transaction':transactionjson})

        print(res.text)


    def validate_transaction(self, transaction):
        print("Validation I am node {} right now".format(self.id))
        # k = 1
        # for r in self.ring:
        #     temp_key = RSA.generate(2048, e=65537)
        #     temp_public_key = temp_key.publickey()
        #     if(r['public_key'] == transaction.sender_address):
        #         print("This transaction was sent to me by Node", r['id'])
        #         k = 0
        # if(k):
        #     print("This transaction was sent to me by myself Node", self.id)

        sender_address=transaction.sender_address
        ##use temp until h is passed humanly
        h= SHA.new(transaction.transaction_myid.encode())
        signature=transaction.signature
        pubkey=sender_address
        verified = PKCS1_v1_5.new(pubkey).verify(h, signature)
        if(verified):
            return True
        else:
            return False


    def add_transaction_to_block(self, transaction):
    	capacity = self.current_block.capacity
    	if(self.chain): # first transaction
            print("I am node with id {} and I am adding transaction ({}) to block ({})".format(self.id, transaction.transaction_id_hex, self.current_block.timestamp))
            self.current_block.add_transaction(transaction)
            #if enough transactions  mine
            print(len(self.current_block.listOfTransactions), capacity)
            if(len(self.current_block.listOfTransactions) == capacity):
                mined_block = self.mine_block(self.current_block)
                print ("Mined block: ", mined_block)
                if(not type(mined_block) == type(-1)):
                    self.chain.add_block_to_chain(mined_block)
                    self.previous_block = None
                    for r in self.ring:
                        start_new_thread(self.broadcast_block, (mined_block, r, ))

                if (not self.previous_block):
                    self.previous_block = self.current_block
                    self.current_block = self.create_new_block(self.current_block.index + 1, self.current_block.currentHash_hex, None, time.time(), self.current_block.difficulty, self.current_block.capacity)
                    print("Creating new block!")
                else:
                    print("Cannot create new block...")
                    while (True):
                        print ("Previous block", self.previous_block)
                        time.sleep(10)
                        if (not self.previous_block):
                            self.previous_block = self.current_block
                            self.current_block = self.create_new_block(self.current_block.index + 1, self.current_block.currentHash_hex, None, time.time(), self.current_block.difficulty, self.current_block.capacity)
                            print("Creating new block!")
                            break
    	else:
    		self.current_block.add_transaction(transaction)


    def mine_block(self, block):
        print("Node {} is mining block {}".format(self.id, block.index))
        block.nonce = 0
        winner = 1
        while ( not (block.myHash(block.nonce).hexdigest().startswith('0'* block.difficulty))):
            block.nonce += 1
            if(self.chain.chain[-1].index == block.index):
                winner = 0
                print("I lost :(")
                break
            # print(block.myHash(block.nonce).hexdigest())
        if(winner):
            block.currentHash = SHA.new((str(block.index)+str(block.previousHash_hex)+str(block.nonce)).encode())
            print("I won (Node {}), broadcasting victory...".format(self.id))
            print("i found nonce {} for block {}".format(block.nonce, block.index))
            return block
        else:
            return -1
        #TODO run a simulation to see if all transactions can happen e.g i have 100$, give 100$ to a and give 100$ to b

    # def valid_proof(.., difficulty=MINING_DIFFICULTY):
    def broadcast_block(self, block, r):
        baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])

        blockjson = jsonpickle.encode(block)
        print("I am node with id {} and I am broadcasting block ({}) to {}".format(self.id, block.timestamp, baseurl))
        res = requests.post(baseurl + "ValidateBlock", json = {'block':blockjson})
        print(res.text)
    # def valid_proof(.., difficulty=MINING_DIFFICULTY):




    #concencus functions

    def validate_block(self, block):
        print("I am node with id {} and I am Validating block ({})".format(self.id, block.timestamp))
        print("The nonce is {} for block {}".format(block.nonce, block.index))
        curr_hash = SHA.new((str(block.index)+str(block.previousHash_hex)+str(block.nonce)).encode())
        if (curr_hash.hexdigest().startswith('0'* block.difficulty)):
            print(block.previousHash_hex)
            print(block.currentHash_hex)
            print(self.chain.chain[-1].currentHash_hex)
            print(len(self.chain.chain))
            if block.previousHash_hex == self.chain.chain[-1].currentHash_hex:
                # if previousHash is same as actual previous hash.self.
                self.previous_block = None
                return True
            else:
                return self.resolve_conflicts(block)
        else:
            return False



    def validate_chain(self, blockchain):
    	print("Validating blockchain...")
    	for block in blockchain.chain:
    		if(block.index > 0):
    			# Block is not genesis
    			self.validate_block(block)
    	print("Blockchain Validated.")

    def resolve_conflicts(self, block):
    	#TODO resolve correct chain
    	print("Resolving Conflicts")
    	return True
