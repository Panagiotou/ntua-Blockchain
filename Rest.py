import requests
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from multiprocessing import Value, Array, Process, Manager, Lock
from block import Block
from node import Node
from blockchain import Blockchain
from wallet import Wallet
from transaction import Transaction
import transaction
import json
import sys, os
import requests
import time
from node import Node
### JUST A BASIC EXAMPLE OF A REST API WITH FLASK

app = Flask(__name__)
CORS(app)
blockchain = Blockchain()

#.......................................................................................



# get all transactions in the blockchain

@app.route('/transactions/get', methods=['GET'])
def get_transactions():
    transactions = blockchain.transactions

    response = {'transactions': transactions}
    return jsonify(response), 200

@app.route('/UpdateRing', methods=['POST'])
def UpdateRing():
    # print("request", request.json)
    if request is None:
        return "Error: Please supply a valid Ring", 400
    data = request.json
    if data is None:
        return "Error: Please supply a valid Ring", 400
    node.ring = list(data.values())

    return "Ring Updated for node {}".format(node.id), 200

def ContactBootstrapNode(baseurl, host, port):
    public_key = node.wallet.public_key
    load = {'public_key': str(public_key), 'ip': host, 'port': port }
    r = requests.post(baseurl + "nodes/register", json = load)
    if(not r.status_code == 200):
        print(r.text)
        exit(1)
    rejson = r.json()
    myid = rejson["id"]
    bootstrap_public_key = rejson["bootstrap_public_key"]
    node.id = myid

    print("I am node with ip {} and my unique id is {}!".format(host, node.id))

if __name__ == '__main__':
    from argparse import ArgumentParser
    node = Node()
    
    baseurl = 'http://{}:{}/'.format("127.0.0.1","5000")
    host = sys.argv[1]
    port = 5000
    ContactBootstrapNode(baseurl, host, port)
    app.run(host=host, port=port, debug=True, use_reloader=False)
