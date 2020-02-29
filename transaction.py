from collections import OrderedDict

import binascii

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import requests
from flask import Flask, jsonify, request, render_template


class Transaction:

    def __init__(self, sender_address, sender_private_key, recipient_address, value):
        ##set
        self.sender_address = sender_address
        self.receiver_address = recipient_address
        self.amount = value
        self.transaction_id = SHA.new((str(sender_address)+str(recipient_address)+str(value) + str(Crypto.Random.get_random_bytes(10))).encode())# το hash του transaction
        self.transaction_inputs = [] # λίστα από Transaction Input
        self.transaction_outputs = [self.transaction_id, self.receiver_address, value] # λίστα από Transaction Output
        # if(not self.sender_address == 0):
        #     self.signature = self.sign_transaction(sender_private_key)


    # def to_dict(self):


    def sign_transaction(self, private_key):
        """
        Sign transaction with private key
        """
        signer = PKCS1_v1_5.new(private_key)
        signature = signer.sign(self.transaction_id)
        return signature
