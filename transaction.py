from collections import OrderedDict

import binascii
import time
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import random
import requests
from flask import Flask, jsonify, request, render_template


def makeRSAjsonSendable(rsa):
    return rsa.exportKey("PEM").decode('ascii')
def makejsonSendableRSA(jsonSendable):
    return RSA.importKey(jsonSendable.encode('ascii'))


class Transaction:

    def __init__(self, sender_address, sender_private_key, recipient_address, value, reals=None, realr=None):
        ##set
        self.sender_address = sender_address
        self.receiver_address = recipient_address
        self.amount = value
        self.reals = reals
        self.realr = realr
        self.rand = Crypto.Random.get_random_bytes(10)
        self.transaction_id = SHA.new((str(sender_address)+str(recipient_address)+str(value) + str(self.rand)).encode())# το hash του transaction
        self.transaction_myid = str(sender_address)+str(recipient_address)+str(value) + str(self.rand)
        #self.transaction_id_sendable = makejsonSendableRSA(self.transaction_id)
        self.transaction_inputs = [] # λίστα από Transaction Input
        self.transaction_outputs = [] # λίστα από Transaction Output
        self.transaction_id_hex=self.transaction_id.hexdigest()
        self.timeCreated = time.time()
        self.timeAdded = None
        self.signature = None
        if(not type(self.sender_address) == type(0)):
            self.signature = self.sign_transaction(sender_private_key)

            # self.signature_sendable =  PKCS1_v1_5.new(self.signature)


    # def to_dict(self):

    def sign_transaction(self, private_key):
        """
        Sign transaction with private key
        """
        signature = PKCS1_v1_5.new(private_key).sign(self.transaction_id)
        return signature

    def verify_transaction(self):
        return True
    def printMe(self):
        sender = self.sender_address
        receiver = self.receiver_address
        if(not self.reals == None):
            sender = self.reals
        if(not self.realr == None):
            receiver = self.realr
        print("\t \t I am transaction ({}) giving {} $ from node {} to node {}".format(self.transaction_id_hex, self.amount, sender, receiver))
