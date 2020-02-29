import blockchain




class Block:
	def __init__(self):
		##set

		self.previousHash = None
		self.timestamp = None
		self.hash = None
		self.nonce = None
		self.listOfTransactions = []

	# def myHash():
	# 	#calculate self.hash


	#def add_transaction(transaction, blockchain):
	#def add_transaction(transaction):
	 	#add a transaction to the block
