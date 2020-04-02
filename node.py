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
PRINTCHAIN = False


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
        self.current_NBCs = []
        self.wallet = None # created with create_wallet()
        self.ring = []
        self.create_wallet()
        self.previous_block = None
        self.current_block = None
        self.block_capacity = None
        self.myip = None
        self.myport = None
        self.completed_transactions = []
        self.validated_transactions = []
        self.all_lock = threading.Lock()

    def create_new_block(self, index, previousHash_hex, nonce, timestamp, difficulty, capacity):
    	return Block(index, previousHash_hex, nonce, timestamp, difficulty, capacity)

    def create_wallet(self):
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
            transaction.transaction_inputs = self.current_NBCs[realsender][1]

            output_id1 = transaction.transaction_id_hex + 'a'
            output1 = [output_id1, transaction.transaction_id_hex, int(realreceiver), amount]
            transaction.transaction_outputs.append(output1)

            output_id2 = transaction.transaction_id_hex + 'b'
            output2 = [output_id2, transaction.transaction_id_hex, int(realsender), self.current_NBCs[int(realsender)][0] - amount]
            transaction.transaction_outputs.append(output2)

        if(transaction.signature):
            transactionjson = jsonpickle.encode(transaction)
            baseurl = 'http://{}:{}/'.format(self.myip, self.myport)
            res = requests.post(baseurl + "ValidateTransaction", json = {'transaction':transactionjson})

        for r in self.ring:
            start_new_thread(self.broadcast_transaction, (transaction,r, ))
        return transaction


    def broadcast_transaction(self, transaction, r):
        baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])
        transactionjson = jsonpickle.encode(transaction)
        res = requests.post(baseurl + "ValidateTransaction", json = {'transaction':transactionjson})



    def validate_transaction(self, transaction):
        sender_address=transaction.sender_address
        h= SHA.new(transaction.transaction_myid.encode())
        signature=transaction.signature
        pubkey=sender_address
        verified = PKCS1_v1_5.new(pubkey).verify(h, signature)
        if (not(verified)):
            return False

        realsender = int(transaction.reals)
        realreceiver = int(transaction.realr)

        if(verified and transaction.amount<=self.current_NBCs[int(realsender)][0]):
            self.current_NBCs[realsender][0] = self.current_NBCs[realsender][0] - transaction.amount
            self.current_NBCs[realsender][1].append(transaction.transaction_id_hex)
            self.current_NBCs[realreceiver][0] = self.current_NBCs[realreceiver][0] + transaction.amount
            self.current_NBCs[realreceiver][1].append(transaction.transaction_id_hex)
            return True

        else:
            return False


    def add_transaction_to_block(self, transaction):
        self.all_lock.acquire()
        for b in self.chain.chain:
            for trans_iter in b.listOfTransactions:
                if(transaction.transaction_id_hex == trans_iter.transaction_id_hex):
                    try:
                        self.all_lock.release()
                    except:
                        pass
                    return False

        for trans_iter in self.completed_transactions:
            if(transaction.transaction_id_hex == trans_iter.transaction_id_hex):
                try:
                    self.all_lock.release()
                except:
                    pass
                return False

        for trans_iter in self.validated_transactions:
            if(transaction.transaction_id_hex == trans_iter.transaction_id_hex):
                try:
                    self.all_lock.release()
                except:
                    pass
                return False

        for trans_iter in self.current_block.listOfTransactions:
            if(transaction.transaction_id_hex == trans_iter.transaction_id_hex):
                try:
                    self.all_lock.release()
                except:
                    pass
                return False
        self.current_block.add_transaction(transaction)
        self.validated_transactions.append(transaction)


        if(len(self.current_block.listOfTransactions) == self.current_block.capacity):
            try:
                self.all_lock.release()
            except:
                pass
            finally:
                self.all_lock.acquire()
            mined_block = self.mine_block()
            self.current_block = self.create_new_block(self.current_block.index + 1, self.current_block.currentHash_hex, 0, time.time(), self.current_block.difficulty, self.current_block.capacity)
            try:
                self.all_lock.release()
            except:
                pass
        else:
            try:
                self.all_lock.release()
            except:
                pass
        return 1

    def mine_block(self):
        self.current_block.nonce = 0
        while ( not (self.current_block.myHash(self.current_block.nonce).hexdigest().startswith('0'* self.current_block.difficulty))):
            self.current_block.nonce += 1
            if (self.current_block.index <= self.chain.chain[-1].index):
                return

        baseurl = 'http://{}:{}/'.format(self.myip, self.myport)
        blockjson = jsonpickle.encode(self.current_block)
        res = requests.post(baseurl + "AddBlock", json = {'block':blockjson})

        for r in self.ring:
            start_new_thread(self.broadcast_block,(self.current_block,r))
        return self.current_block

    def broadcast_block(self, block, r):
        baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])

        blockjson = jsonpickle.encode(block)
        res = requests.post(baseurl + "AddBlock", json = {'block':blockjson})




    def validate_block(self, block):
        curr_hash = SHA.new((str(block.index)+str(block.previousHash_hex)+str(block.nonce)).encode())
        if (curr_hash.hexdigest().startswith('0'* block.difficulty) and block.previousHash_hex == self.chain.chain[-1].currentHash_hex):
            return True
        else:
            return False



    def validate_chain(self, blockchain):
    	for block in blockchain.chain:
    		if(block.index > 0):
    			self.validate_block(block)

    def resolve_conflicts(self):

        somechain = []
        node_id = []
        current_NBCs = []
        NBCs = []
        vt = []
        for r in self.ring:
            baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])
            res = requests.get(baseurl + "Chain").json()
            somechain.append(jsonpickle.decode(res["chain"]))
            node_id.append(res["id"])
            current_NBCs.append(res["current_NBCs"])
            NBCs.append(res["NBCs"])
            vt.append(jsonpickle.decode(res["VT"]))
        maxlen = len(somechain[0].chain)
        for i in range(len(somechain)):
            if(len(somechain[i].chain) > maxlen):
                maxlen = len(somechain[i].chain)

        k = 0
        changed = 0

        for i in range(len(somechain)):
            if(len(somechain[i].chain) == maxlen):
                k = i
                changed = 1
                break

        if( (maxlen == len(self.chain.chain) and self.id < node_id[k]) or (len(self.chain.chain) > maxlen)):
            return

        if(changed):
            self.chain = somechain[k]
            self.current_NBCs = current_NBCs[k]
            self.NBCs = NBCs[k]
            self.validated_transactions = vt[k]
        return
