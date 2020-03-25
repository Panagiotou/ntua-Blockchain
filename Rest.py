import requests
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from multiprocessing import Value, Array, Process, Manager, Lock
from block import Block
from node import Node
from blockchain import Blockchain
from wallet import Wallet
from _thread import *
import threading
import transaction
import json
import sys, os
import time
import jsonpickle
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from copy import deepcopy
from Crypto.Signature import PKCS1_v1_5
PRINTCHAIN = False


app = Flask(__name__)
CORS(app)
blockchain = Blockchain()

#.......................................................................................

def makeRSAjsonSendable(rsa):
    return rsa.exportKey("PEM").decode('ascii')

def makejsonSendableRSA(jsonSendable):
    return RSA.importKey(jsonSendable.encode('ascii'))

def read_transaction():
    time.sleep(2)
    print("Reading input transactions")
    f = open("5nodes_small/transactions" + str(node.id) + ".txt", "r")
    print(node.ring)
    for line in f:
        id, amount = (line).split()
        for n in node.ring:
            if int(n['id']) == int(id[-1]):
                # time.sleep(1)
                # print("LINE", line)
                start_new_thread(node.create_transaction, (node.wallet.address, node.wallet.private_key, n['public_key'], int(amount),))
                # node.create_transaction(node.wallet.address, node.wallet.private_key, n['public_key'], int(amount))
                break

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
    ring = list(data.values())
    r1 = None
    for r in ring:
        r1 = r
        r1['public_key'] = makejsonSendableRSA(r1['public_key'])
        print(r1)
        node.ring.append(r1)
    # print("My ring was updated by bootstrap Node!")
    read_transaction()
    return "Ring Updated for node {}".format(node.id), 200

@app.route('/AddBlock', methods=['POST'])
def AddBlock():
    if request is None:
        return "Error: Please supply a valid Block", 400
    data = request.json
    if data is None:
        return "Error: Please supply a valid Block", 400

    block = jsonpickle.decode(data["block"])
    if(block.index > 0):
        valid = node.validate_block(block)
        print("validating block")
        block.printMe()
        print("result", valid)

        print("chain at the moment")
        if(node.chain.chain):
            node.chain.printMe()

        if(valid):
            node.chain.add_block_to_chain(block)

            node.previous_block = block
            node.current_block = node.create_new_block(block.index + 1, block.currentHash_hex, 0, time.time(), block.difficulty, block.capacity)
            #node.NBCs = node.current_NBCs
            for t in block.listOfTransactions:
                outputs = t.transaction_outputs
                id = outputs[0][1]
                realreceiver = outputs[0][2]
                realsender = outputs[1][2]
                amount = outputs[0][3]
                node.NBCs[realreceiver][0] = node.NBCs[realreceiver][0] + amount
                node.NBCs[realreceiver][1].append(id)
                node.NBCs[realsender][0] = node.NBCs[realsender][0] - amount

            for tran_iter in block.listOfTransactions:
                node.completed_transactions.append(tran_iter)

            #TODO run actual transactions
            # node.all_lock.release()
        else:
            node.resolve_conflicts()
            # start_new_thread(node.resolve_conflicts,())
            # node.all_lock.release()
    try:
        node.all_lock.release()
    except:
        pass
    return "OK", 200


@app.route('/ValidateTransaction', methods=['POST'])
def ValidateTransaction():
    # if(node.id == 1):
    #     print("Node 1 sleeping")
    #     time.sleep(5)
    # print("request", request.json)
    if request is None:
        return "Error: Please supply a valid Transaction", 400
    data = request.json
    if data is None:
        return "Error: Please supply a valid Transaction", 400

    transaction = jsonpickle.decode(data["transaction"])
    valid = node.validate_transaction(transaction)
    if(valid):
        # node.current_block.lock.acquire()
        # node.all_lock.acquire()
        node.add_transaction_to_block(transaction)
        # node.all_lock.release()

        # node.current_block.lock.release()

        return "Transaction Validated by Node {} !".format(node.id), 200
    else:
        return "Error: Not valid!", 400

@app.route('/Live', methods=['GET'])
def Live():
    return "I am alive!", 200


def ContactBootstrapNode(baseurl, host, port):
    public_key = node.wallet.public_key
    load = {'public_key': makeRSAjsonSendable(public_key), 'ip': host, 'port': port }
    r = requests.post(baseurl + "nodes/register", json = load)
    if(not r.status_code == 200):
        print(r.text)
        exit(1)
    rejson = r.json()
    myid = rejson["id"]
    bootstrap_public_key = makejsonSendableRSA(rejson["bootstrap_public_key"])
    block_capacity = rejson["block_capacity"]
    NBCs = rejson['NBCs']
    current_NBCs = rejson['current_NBCs']
    node.NBCs = NBCs
    node.current_NBCs = current_NBCs
    node.id = myid
    node.myip = host
    node.myport = port
    rejson['start_ring']['public_key'] = makejsonSendableRSA(rejson['start_ring']['public_key'])
    node.ring.append(rejson['start_ring'])
    # print("I am node with ip {} and my unique id is {}!".format(host, node.id))

    blockchain = jsonpickle.decode(rejson["blockchain"])
    node.chain = blockchain
    # node.validate_chain(blockchain)
    #if(len(blockchain.chain) == 1):
    node.previous_block = None
    node.current_block = jsonpickle.decode(rejson["current_block"])

    # print("Now I can create transactions!")
@app.route('/Chain', methods=['GET'])
def Chain():
    return {'chain': jsonpickle.encode(node.chain), 'previous_block': jsonpickle.encode(node.previous_block), 'current_block': jsonpickle.encode(node.current_block), 'current_NBCs': node.current_NBCs, 'NBCs': node.NBCs}

@app.route('/PrintChain', methods=['GET'])
def PrintChain():
    node.chain.printMe()
    return "OK", 200

@app.route('/PrintWallet', methods=['GET'])
def PrintWallet():
    print("NBCs")
    for nbc in node.NBCs:
        print("\t", nbc[0])
    return "OK", 200

if __name__ == '__main__':
    from argparse import ArgumentParser
    node = Node()

    baseurl = 'http://{}:{}/'.format("127.0.0.1","5000")
    host = sys.argv[1]
    port = 5000
    ContactBootstrapNode(baseurl, host, port)
    app.run(host=host, port=port, debug=True, use_reloader=False)
