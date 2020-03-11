import blockchain
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5



class Block:
	def __init__(self, index, previousHash, nonce, timestamp, difficulty):
		##set
		self.index = index
		self.previousHash = previousHash
		self.nonce = nonce
		self.timestamp = timestamp
		self.currentHash = self.myHash()
		self.listOfTransactions = []
		self.difficulty = difficulty

	def myHash(self):
		self.currentHash = SHA.new((str(self.index)+str(self.previousHash)+str(self.timestamp)+str(self.nonce)).encode())
		return SHA.new((str(self.index)+str(self.previousHash)+str(self.timestamp)+str(self.nonce)).encode())

	def add_transaction(self, transaction):
		self.listOfTransactions.append(transaction)
