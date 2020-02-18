import binascii

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4



class Wallet:

	def __init__(self):
		##set
		bits=2048
		new_key = RSA.generate(bits, e=65537)
		self.public_key = new_key.publickey().exportKey()
		self.private_key = new_key.exportKey()
		#self_address
		#self.transactions

	#def balance():
