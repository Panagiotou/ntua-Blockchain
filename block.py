import blockchain
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5



class Block:
	def __init__(self, index, previousHash_hex, nonce, timestamp, difficulty, capacity):
		##set
		self.index = index
		#self.previousHash = previousHash
		self.previousHash_hex = previousHash_hex
		self.nonce = nonce
		self.timestamp = timestamp
		self.currentHash = SHA.new((str(self.index)+str(self.previousHash_hex)+str(self.nonce)).encode())
		self.currentHash_hex = self.currentHash.hexdigest()
		self.listOfTransactions = []
		# if(not type(previousHash) == type(0)):
		# 	self.previousHash_hex = previousHash.hexdigest()
		# 	self.currentHash_hex = self.currentHash.hexdigest()
		self.difficulty = difficulty
		self.capacity = capacity
	def __eq__(self, other):
		"""Overrides the default implementation"""
		ret = (self.index == other.index and self.previousHash == other.previousHash and self.timestamp == other.timestamp)
		return ret

	def myHash(self, nonce):
		# self.currentHash = SHA.new((str(self.index)+str(self.previousHash)+str(self.timestamp)+str(self.nonce)).encode())
		return SHA.new((str(self.index)+str(self.previousHash_hex)+str(self.nonce)).encode())

	def add_transaction(self, transaction):
		self.listOfTransactions.append(transaction)

	def printMe(self):
		print("\t I am block with index", self.index)
		print("\t My Transaction list contains:")
		for t in self.listOfTransactions:
			t.printMe()
