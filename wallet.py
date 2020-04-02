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
		bits=2048
		new_key = RSA.generate(bits, e=65537)
		self.private_key = new_key
		self.public_key = new_key.publickey()
		self.address = self.public_key
