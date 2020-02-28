import block
from wallet import Wallet
from transaction import Transaction
# to broadcast_transaction
from flask import Flask, render_template
from flask_socketio import send,  SocketIO

class Node:
	def __init__(self):
		#self.NBC=100;
		##set

		#self.chain
		self.current_id_count = None # +1 every time a node is added
		self.id = None # 0...n-1
		self.NBCs = None
		self.wallet = None # created with create_wallet()
		self.ring[]   #here we store information for every node, as its id, its address (ip:port) its public key and its balance
		self.create_wallet()



	#def create_new_block():

	def create_wallet(self):
		#create a wallet for this node, with a public key and a private key
		self.wallet = Wallet()


	# def register_node_to_ring():
	# 	#add this node to the ring, only the bootstrap node can add a node to the ring after checking his wallet and ip:port address
	# 	#bottstrap node informs all other nodes and gives the request node an id and 100 NBCs


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



	def validate_transaction(signature, message, public_key):
	    #use of signature and NBCs balance
		h = SHA.new(message)
		verifier = PKCS1_v1_5.new(public_key)
		if verifier.verify(h, signature):
			print("The signature is authentic.")
		else:
			print("The signature is not authentic.")


	# def add_transaction_to_block():
	# 	#if enough transactions  mine
	#
	#
	#
	# def mine_block():
	#
	#
	#
	# def broadcast_block():
	#
	#
	#
	#
	# def valid_proof(.., difficulty=MINING_DIFFICULTY):
	#
	#
	#
	#
	# #concencus functions
	#
	# def valid_chain(self, chain):
	# 	#check for the longer chain accroose all nodes
	#
	#
	# def resolve_conflicts(self):
	# 	#resolve correct chain
