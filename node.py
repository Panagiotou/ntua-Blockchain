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
DEBUG = True
PRINTCHAIN = True
v_lock = threading.Lock()

def makeRSAjsonSendable(rsa):
    return rsa.exportKey("PEM").decode('ascii')
def makejsonSendableRSA(jsonSendable):
    return RSA.importKey(jsonSendable.encode('ascii'))

class Node:
    def __init__(self):

        self.chain = None
        self.current_id_count = None # +1 every time a node is added
        self.id = None # 0...n-1
        self.NBCs = []
        self.wallet = None # created with create_wallet()
        self.ring = []   #here we store information for every node, as its id, its address (ip:port) its public key and its balance
        self.create_wallet()
        self.previous_block = None
        self.current_block = None
        self.block_capacity = None
        self.myip = None
        self.myport = None
        self.completed_transactions = []
        self.all_lock = threading.Lock()

    def create_new_block(self, index, previousHash_hex, nonce, timestamp, difficulty, capacity):
    	return Block(index, previousHash_hex, nonce, timestamp, difficulty, capacity)

    def create_wallet(self):
    	#create a wallet for this node, with a public key and a private key
    	self.wallet = Wallet()

    def create_transaction(self, sender, sender_private_key, receiver, amount):
        realsender = None
        realreceiver = None
        if(DEBUG):
            if(type(sender) == type(0)):
                realsender = "genesis"
                realreceiver = "0"
            for r in self.ring:
                try:
                    if(r['public_key'] == sender):
                        realsender = r['id']
                except:
                    pass
                try:
                    if(r['public_key'] == makeRSAjsonSendable(sender)):
                        realsender = r['id']
                except:
                    pass
                try:
                    if(sender == self.wallet.public_key):
                        realsender = self.id
                except:
                    pass
                try:
                    if(makeRSAjsonSendable(sender) == makeRSAjsonSendable(self.wallet.public_key)):
                        realsender = self.id
                except:
                    pass
                try:
                    if(r['public_key'] == receiver):
                        realreceiver = r['id']
                except:
                    pass
                try:
                    if(r['public_key'] == makeRSAjsonSendable(receiver)):
                        realreceiver = r['id']
                except:
                    pass
                try:
                    if(receiver == self.wallet.public_key):
                        realreceiver = self.id
                except:
                    pass
                try:
                    if(makeRSAjsonSendable(receiver) == makeRSAjsonSendable(self.wallet.public_key)):
                        realreceiver = self.id
                except:
                    pass
        transaction = Transaction(sender, sender_private_key, receiver, amount, reals=realsender, realr=realreceiver)

        if (not realsender == "genesis"):
            transaction.transaction_inputs = self.NBCs[realsender][1]

            output_id1 = transaction.transaction_id_hex + 'a'
            output1 = [output_id1, transaction.transaction_id, int(realreceiver), amount]
            transaction.transaction_outputs.append(output1)

            output_id2 = transaction.transaction_id_hex + 'b'
            output2 = [output_id2, transaction.transaction_id, int(realsender), self.NBCs[int(realsender)][0] - amount]
            transaction.transaction_outputs.append(output2)

        if(transaction.signature):
            transactionjson = jsonpickle.encode(transaction)
            baseurl = 'http://{}:{}/'.format(self.myip, self.myport)
            res = requests.post(baseurl + "ValidateTransaction", json = {'transaction':transactionjson})
        self.all_lock.acquire()
        print("Created transaction")
        transaction.printMe()
        self.all_lock.release()
        start_new_thread(self.broadcast_transaction, (transaction, ))
            # self.broadcast_transaction(transaction, baseurl)
        return transaction


    def broadcast_transaction(self, transaction):
        for r in self.ring:
            baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])
            transactionjson = jsonpickle.encode(transaction)
            # print("I am node with id {} and I am broadcasting the transaction ({}) to node {} with url {}".format(self.id, transaction.transaction_id_hex,  r['id'], baseurl))

            res = requests.post(baseurl + "ValidateTransaction", json = {'transaction':transactionjson})

        # print(res.text)


    def validate_transaction(self, transaction):
        # print("i am node {} validating transaction:".format(self.id))
        # transaction.printMe()
        v_lock.acquire()
        print("Validating Transaction")
        transaction.printMe()

        sender_address=transaction.sender_address
        ##use temp until h is passed humanly
        h= SHA.new(transaction.transaction_myid.encode())
        signature=transaction.signature
        pubkey=sender_address
        verified = PKCS1_v1_5.new(pubkey).verify(h, signature)
        if (not(verified)):
            print("Result False")
            v_lock.release()
            return False

        #Check duplicate
        for trans_iter in self.completed_transactions:
            if(transaction.transaction_id_hex == trans_iter.transaction_id_hex):
            ##duplicate transaction
                v_lock.release()
                return False


        realsender = transaction.reals
        if(verified and transaction.amount<=self.NBCs[int(realsender)][0]):
            print("Result True")
            v_lock.release()
            return True

        else:
            print("Result False")
            v_lock.release()
            return False


    def add_transaction_to_block(self, transaction, block):
        if(self.chain):
            self.all_lock.acquire()
            print('Trani', transaction.transaction_id_hex)
            block.printMe()
            print(block.isInBlock(transaction.transaction_id_hex))
            print(self.chain.isInChain(transaction.transaction_id_hex))
            if(self.chain.isInChain(transaction.transaction_id_hex) or block.isInBlock(transaction.transaction_id_hex)):
                print("Transaction was already in chain or in block")
                transaction.printMe()
                self.all_lock.release()
                return 0
            else:
                self.all_lock.release()
        self.all_lock.acquire()
        # transaction.printMe()
        capacity = block.capacity
        while(len(block.listOfTransactions) == capacity):
            print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            self.previous_block = block
            self.current_block = self.create_new_block(block.index + 1, block.currentHash_hex, None, time.time(), block.difficulty, block.capacity)
            self.all_lock.release()
            mined_block = self.mine_block(block)
            # self.all_lock.release()
            return
        block.add_transaction(transaction)
        print(len(block.listOfTransactions), capacity)
        if(len(block.listOfTransactions) < capacity):
            self.all_lock.release()
        if(len(block.listOfTransactions) == capacity):
            print("AAAA")
            self.previous_block = block
            self.current_block = self.create_new_block(block.index + 1, block.currentHash_hex, None, time.time(), block.difficulty, block.capacity)
            self.all_lock.release()
            mined_block = self.mine_block(block)
            # self.all_lock.release()

        return 1

    def mine_block(self, block):
        # print("Node {} is mining block {}".format(self.id, block.index))
        block.nonce = 0
        while ( not (block.myHash(block.nonce).hexdigest().startswith('0'* block.difficulty))):
            block.nonce += 1
            # print(block.myHash(block.nonce).hexdigest())

        print("Validate own block")
        baseurl = 'http://{}:{}/'.format(self.myip, self.myport)
        blockjson = jsonpickle.encode(block)
        res = requests.post(baseurl + "AddBlock", json = {'block':blockjson})
        print("Done")

        start_new_thread(self.broadcast_block,(block,))
        return block

    # def valid_proof(.., difficulty=MINING_DIFFICULTY):
    def broadcast_block(self, block):
        for r in self.ring:
            baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])

            blockjson = jsonpickle.encode(block)
            # print("I am node with id {} and I am broadcasting block ({}) to {}".format(self.id, block.timestamp, baseurl))
            res = requests.post(baseurl + "AddBlock", json = {'block':blockjson})
        # print(res.text)
    # def valid_proof(.., difficulty=MINING_DIFFICULTY):




    #concencus functions

    def validate_block(self, block):
        # print("I am node with id {} and I am Validating block ({})".format(self.id, block.timestamp))
        # print("The nonce is {} for block {}".format(block.nonce, block.index))
        curr_hash = SHA.new((str(block.index)+str(block.previousHash_hex)+str(block.nonce)).encode())
        if (curr_hash.hexdigest().startswith('0'* block.difficulty) and block.previousHash_hex == self.chain.chain[-1].currentHash_hex):
            return True
        else:
            return False



    def validate_chain(self, blockchain):
    	# print("Validating blockchain...")
    	for block in blockchain.chain:
    		if(block.index > 0):
    			# Block is not genesis
    			self.validate_block(block)
    	# print("Blockchain Validated.")

    def resolve_conflicts(self):
        maxlen = len(self.chain.chain)
        k = 0
        old_chain = self.chain
        old_curr = self.current_block
        tempchain = self.chain
        for r in self.ring:
            baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])
            res = requests.get(baseurl + "Chain").json()
            somechain = jsonpickle.decode(res["chain"])
            if(not somechain.isCorrect()):
                continue
            self.all_lock.acquire()
            if(len(somechain.chain) > maxlen):
                k = 1
                tempchain = somechain
                maxlen = len(somechain.chain)
                self.chain = tempchain
                self.current_block = jsonpickle.decode(res["curr"])
                print("RESOLVE conflicts chain updated")
            self.all_lock.release()
        if(k):
            print("Old chain")
            old_chain.printMe()
            print("New Chain")
            self.chain.printMe()
            print("old curr")
            old_curr.printMe()
            print("new curr")
            self.current_block.printMe()
        return
