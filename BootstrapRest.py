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
import time


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

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    if request is None:
        return "Error: Please supply a valid Node", 400
    data = request.json
    if data is None:
        return "Error: Please supply a valid Node", 400
    # print("Add node with public_key", data["public_key"])
    if(BootstrapDict['nodeCount'] >= BootstrapDict['N']):
        return "Error: System is full", 405
    lock = Lock()
    lock.acquire()
    BootstrapDict['nodeCount'] += 1
    BootstrapDictInstance = BootstrapDict.copy()
    lock.release()
    # if(BootstrapDict['nodeCount'] == 2):
    #     print("Node 2 Sleeping")
    #     time.sleep(10)
    #     print("Node 2 Awake")

    # for node in nodes:
    #     blockchain.register_node(node)
    #
    # response = {
    #     'message': 'New nodes have been added',
    #     'total_nodes': list(blockchain.nodes),
    # }
    # return jsonify(response), 201

    # transaction
    amount = 100
    transaction = node.create_transaction(bootstrap_public_key,  node.wallet.private_key, data['public_key'], amount)
    # add transaction to a block
    # block.listOfTransactions.append(transaction)
    # return jsonify({'id':BootstrapDict['nodeCount']-1, 'bootstrap_public_key':BootstrapDict['bootstrap_public_key']})

    return jsonify({'id':BootstrapDictInstance['nodeCount']-1, 'bootstrap_public_key':BootstrapDictInstance['bootstrap_public_key']})

# run it once fore every node

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    manager = Manager()

    BootstrapDict = manager.dict()

    N = 5   #Number of nodes i  the system
    nodeCount = 1
    bootstrap_public_key = ""

    # create bootstrap node
    node = Node()
    node.id = 0
    bootstrap_public_key = node.wallet.public_key

    BootstrapDict['nodeCount'] = nodeCount
    BootstrapDict['bootstrap_public_key'] = bootstrap_public_key
    BootstrapDict['N'] = N
    # create genesis block
    genesis_block = Block()
    genesis_block.previousHash=1
    genesis_block.nonce=0

    # first transaction
    amount = 100*N
    first_transaction = node.create_transaction(0, None, bootstrap_public_key, amount)
    genesis_block.listOfTransactions.append(first_transaction)
    # first transaction does not have a previousOutputId, transaction_inputs = []

    app.run(host='127.0.0.1', port=port, debug=True, use_reloader=False)
