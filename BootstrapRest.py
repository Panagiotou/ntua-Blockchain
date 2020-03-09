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
from _thread import *
import threading
import jsonpickle
### JUST A BASIC EXAMPLE OF A REST API WITH FLASK

app = Flask(__name__)
CORS(app)

def makeRSAjsonSendable(rsa):
    return rsa.exportKey("PEM").decode('ascii')
def makejsonSendableRSA(jsonSendable):
    return RSA.importKey(jsonSendable.encode('ascii'))

#.............................................................
def FirstBroadcast(ring):
    for r in ring:
        baseurl = 'http://{}:{}/'.format(r['ip'],r['port'])
        ringWithoutSelf = {}
        u = 0
        for k in ring:
            if(not k['ip'] == r['ip']):
                ringWithoutSelf[str(u)] = k

        load = ringWithoutSelf

        while(True):
            try:
                r = requests.get(baseurl)
                r.raise_for_status()
            except:
                break

        resRing = requests.post(baseurl + "UpdateRing", json = load)
        print(resRing.text)
# get all transactions in the blockchain

# @app.route('/transactions/get', methods=['GET'])
# def get_transactions():
#     transactions = blockchain.transactions
#
#     response = {'transactions': transactions}
#     return jsonify(response), 200

@app.route('/ValidateBlock', methods=['POST'])
def ValidateBlock():
    # print("request", request.json)
    if request is None:
        return "Error: Please supply a valid Block", 400
    data = request.json
    if data is None:
        return "Error: Please supply a valid Block", 400

    block = jsonpickle.decode(data["block"])
    if(block.index > 0):
        valid = node.validate_block(block)
        if(valid):
            print("Block is Valid")
            node.add_block_to_chain(block)
            #TODO run actual transactions
            return "Block Validated!", 200
        else:
            print("Something went wrong, block is invalid")
            return "Block can not be validated!", 400

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    if request is None:
        return "Error: Please supply a valid Node", 400
    data = request.json
    if data is None:
        return "Error: Please supply a valid Node", 400

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

    # transaction
    amount = 100
    transaction = node.create_transaction(bootstrap_public_key,  node.wallet.private_key, data['public_key'], amount)
    node.ring.append({'id': BootstrapDictInstance['nodeCount']-1, 'ip': data['ip'], 'port': data['port'], 'public_key': data['public_key'], 'balance': 0})
    if(BootstrapDict['nodeCount'] == BootstrapDict['N']):
        start_new_thread(FirstBroadcast,(node.ring, ))

    blockchainjson = jsonpickle.encode(blockchain)

    print("Added Node with id {}, to the system".format(BootstrapDictInstance['nodeCount']-1))
    return jsonify({'id':BootstrapDictInstance['nodeCount']-1, 'bootstrap_public_key':makeRSAjsonSendable(BootstrapDictInstance['bootstrap_public_key']), 'blockchain': blockchainjson, 'block_capacity': BLOCK_CAPACITY})

# run it once fore every node

if __name__ == '__main__':
    from argparse import ArgumentParser
    BLOCK_CAPACITY = 100
    blockchain = Blockchain()


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
    node.block_capacity = BLOCK_CAPACITY

    bootstrap_public_key = node.wallet.public_key

    BootstrapDict['nodeCount'] = nodeCount
    BootstrapDict['bootstrap_public_key'] = bootstrap_public_key
    BootstrapDict['N'] = N
    # create genesis block
    genesis_block = node.create_new_block(0, 1, 0, time.time()) # index = 0, previousHash = 1, nonce = 0
    # first transaction
    amount = 100*N
    first_transaction = node.create_transaction(0, None, bootstrap_public_key, amount)
    node.add_transaction_to_block(first_transaction, genesis_block, BLOCK_CAPACITY)
    blockchain.add_block_to_chain(genesis_block)
    node.chain = blockchain
    print("Genesis block, added to blockchain")
    # Create Second Block index is 2
    node.previous_block = genesis_block
    node.current_block = node.create_new_block(1, genesis_block.currentHash, None, time.time())

    app.run(host='127.0.0.1', port=port, debug=True, use_reloader=False)
