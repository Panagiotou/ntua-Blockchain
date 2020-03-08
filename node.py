from block import Block
from wallet import Wallet
from transaction import Transaction
# to broadcast_transaction
from flask import Flask, render_template
from flask_socketio import send,  SocketIO
import time

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
#
class Node:
	def __init__(self):

		self.chain = None
		self.current_id_count = None # +1 every time a node is added
		self.id = None # 0...n-1
		self.NBCs = None
		self.wallet = None # created with create_wallet()
		self.ring = []   #here we store information for every node, as its id, its address (ip:port) its public key and its balance
		self.create_wallet()


	def create_new_block(self, index, previousHash, nonce, timestamp):
		return Block(index, previousHash, nonce, timestamp)

	def create_wallet(self):
		#create a wallet for this node, with a public key and a private key
		self.wallet = Wallet()

	def create_transaction(self, sender, sender_private_key, receiver, amount):
		transaction = Transaction(sender, sender_private_key, receiver, amount)
		# transaction.transaction_inputs = ...
		return transaction

	 	# remember to broadcast it


	#@socketio.on('json')
	def broadcast_transaction(json):
	# can only be called from a SocketIO event handler.
	# Parameters:
	# send a JSON blob, json = True
		send(json, json=True, broadcast = True)



	# def validate_transaction(signature, message, public_key):
	def validate_transaction(self, transaction):
		return True
		#TODO
	    # #use of signature and NBCs balance
		# h = SHA.new(message)
		# verifier = PKCS1_v1_5.new(public_key)
		# if verifier.verify(h, signature):
		# 	print("The signature is authentic.")
		# 	return True
		# else:
		# 	print("The signature is not authentic.")
		# 	return False


	def add_transaction_to_block(self, transaction, block, capacity):
		if(self.validate_transaction(transaction)):
			block.add_transaction(transaction)
			#if enough transactions  mine
			if(len(block.listOfTransactions) == capacity):
				mined_block = self.mine_block(block)
				# what hapens after block is mined???
				#TODO

	def mine_block(self, block):
		#TODO
		print("Mining block")
		self.broadcast_block(block)
		#TODO run a simulation to see if all transactions can happen e.g i have 100$, give 100$ to a and give 100$ to b

	def broadcast_block(self, block):
		for r in self.ring:
			baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])

			blockjson = jsonpickle.encode(block)

			res = requests.post(baseurl + "ValidateBlock", json = {'block':blockjson})
			print(res.text)
	# def valid_proof(.., difficulty=MINING_DIFFICULTY):




	#concencus functions

	def validate_block(self, block):
		print("Validating Block")
		# if(block.gethash has number of zeros...)
		if block.previousHash == self.chain[-1].currentHash:
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

	def resolve_conflicts(self):
		#TODO resolve correct chain
		print("Resolving")
