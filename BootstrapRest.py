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
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
PRINTCHAIN = False



### JUST A BASIC EXAMPLE OF A REST API WITH FLASK
def read_transaction():
    time.sleep(1)
    print("Reading input transactions")
    f = open("3nodes_small/transactions" + str(node.id) + ".txt", "r")
    print(node.ring)
    for line in f:
        id, amount = (line).split()
        for n in node.ring:
            if int(n['id']) == int(id[-1]):
                time.sleep(1)
                # print("LINE", line)
                start_new_thread(node.create_transaction, (node.wallet.address, node.wallet.private_key, n['public_key'], int(amount),))
                # node.create_transaction(node.wallet.address, node.wallet.private_key, n['public_key'], int(amount))
                break

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
        # ringWithoutSelf['0'] = {'id': 0, 'ip': '127.0.0.1', 'port': '5000', 'public_key': node.wallet.public_key, 'balance': 0}

        u = 0
        for k in ring:
            if(not k['ip'] == r['ip']):
                ringWithoutSelf[str(u)] = k
                u += 1

        load = ringWithoutSelf

        while(True):
            try:
                r = requests.get(baseurl + "Live")
                r.raise_for_status()
            except:
                time.sleep(0.1)
            else:
                break

        resRing = requests.post(baseurl + "UpdateRing", json = load)
        # print(resRing.text)
    read_transaction()

def MakeFirstTransaction(pk, ip , port):
    amount = 100
    baseurl = 'http://{}:{}/'.format(ip, port)
    while(True):
        try:
            r = requests.get(baseurl + "Live")
            r.raise_for_status()
        except:
            time.sleep(0.1)
        else:
            break
    transaction = node.create_transaction(bootstrap_public_key,  node.wallet.private_key, pk, amount)
    return

# get all transactions in the blockchain

# @app.route('/transactions/get', methods=['GET'])
# def get_transactions():
#     transactions = blockchain.transactions
#
#     response = {'transactions': transactions}
#     return jsonify(response), 200

@app.route('/AddBlock', methods=['POST'])
def AddBlock():
    if request is None:
        return "Error: Please supply a valid Block", 400
    data = request.json
    if data is None:
        return "Error: Please supply a valid Block", 400
    # print("is alr locked?", node.all_lock.locked())
    # while(node.all_lock.locked()):
    #     # print("waiting")
    #     time.sleep(1)

    node.all_lock.acquire()
    block = jsonpickle.decode(data["block"])
    if(block.index > 0):
        valid = node.validate_block(block)
        print("validating block")
        block.printMe()
        print("result", valid)

        print("chain at the moment")
        if(node.chain.chain):
            node.chain.printMe()
        # print("validating block")
        # block.printMe()
        # print("result", valid)
        if(valid):
            node.chain.add_block_to_chain(block)
            #node.NBCs = node.current_NBCs
            for t in block.listOfTransactions:
                outputs = t.transaction_outputs
                id = outputs[0][1]
                realreceiver = outputs[0][2]
                realsender = outputs[1][2]
                amount = outputs[0][3]
                t.printMe()
                print("Before=", node.NBCs)
                node.chain.printMe()
                node.NBCs[realreceiver][0] = node.NBCs[realreceiver][0] + amount
                node.NBCs[realreceiver][1].append(id)
                node.NBCs[realsender][0] = node.NBCs[realsender][0] - amount
                # node.NBCs[realsender][1].append(id)
            #make history of completed transactions
            for tran_iter in block.listOfTransactions:
                node.completed_transactions.append(tran_iter)

            #TODO run actual transactions
            node.all_lock.release()
        else:
            node.all_lock.release()
            start_new_thread(node.resolve_conflicts,())

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
        node.current_block.lock.acquire()
        node.add_transaction_to_block(transaction, node.current_block, node.previous_block)
        node.current_block.lock.release()
        # realsender = int(transaction.reals)
        # realreceiver = int(transaction.realr)
        # node.current_NBCs[realsender][0] = node.current_NBCs[realsender][0] - transaction.amount
        # node.current_NBCs[realsender][1].append(transaction.transaction_id_hex)
        # node.current_NBCs[realreceiver][0] = node.current_NBCs[realreceiver][0] + transaction.amount
        # node.current_NBCs[realreceiver][1].append(transaction.transaction_id_hex)

        return "Transaction Validated by Node {} !".format(node.id), 200
    else:
        return "Error: Not valid!", 400

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

    node.ring.append({'id': BootstrapDictInstance['nodeCount']-1, 'ip': data['ip'], 'port': data['port'], 'public_key': data['public_key'], 'balance': 0})
    if(BootstrapDict['nodeCount'] == BootstrapDict['N']):
        start_new_thread(FirstBroadcast,(node.ring, ))

    blockchainjson = jsonpickle.encode(blockchain)
    start_new_thread(MakeFirstTransaction,(data['public_key'], data['ip'], data['port'],))
    # print("Added Node with id {}, to the system".format(BootstrapDictInstance['nodeCount']-1))
    return  jsonify({'id':BootstrapDictInstance['nodeCount']-1, 'bootstrap_public_key':makeRSAjsonSendable(BootstrapDictInstance['bootstrap_public_key']),\
     'blockchain': blockchainjson, 'block_capacity': BLOCK_CAPACITY,\
      'start_ring': {'id': 0, 'ip': '127.0.0.1', 'port': '5000', 'public_key':makeRSAjsonSendable(BootstrapDictInstance['bootstrap_public_key']), 'balance': 0}\
      , 'current_block': jsonpickle.encode(node.current_block), 'NBCs': node.NBCs, 'current_NBCs': node.current_NBCs})

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
    BLOCK_CAPACITY = 2
    MINING_DIFFICULTY = 4
    N = 3  #Number of nodes i  the system

    blockchain = Blockchain()


    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    manager = Manager()

    BootstrapDict = manager.dict()
    nodeCount = 1
    bootstrap_public_key = ""

    # create bootstrap node
    node = Node()
    node.id = 0
    node.myip = '127.0.0.1'
    node.myport = port

    bootstrap_public_key = node.wallet.public_key

    BootstrapDict['nodeCount'] = nodeCount
    BootstrapDict['bootstrap_public_key'] = bootstrap_public_key
    BootstrapDict['N'] = N
    # create genesis block
    genesis_block = node.create_new_block(0, 1, 0, time.time(), MINING_DIFFICULTY, BLOCK_CAPACITY) # index = 0, previousHash = 1, nonce = 0, capacity = BLOCK_CAPACITY
    node.current_block = genesis_block
    # first transaction
    amount = 100*N
    first_transaction = node.create_transaction(0, None, bootstrap_public_key, amount)
    node.add_transaction_to_block(first_transaction, genesis_block, genesis_block)
    blockchain.add_block_to_chain(genesis_block)
    node.chain = blockchain
    if(PRINTCHAIN): node.chain.printMe()
    # print("Genesis block, added to blockchain")
    # Create Second Block index is 2
    node.previous_block = None
    node.current_block = node.create_new_block(1, genesis_block.currentHash_hex, None, time.time(), MINING_DIFFICULTY, BLOCK_CAPACITY)

    inputs = []
    inputs.append(first_transaction.transaction_id_hex)
    node.NBCs.append([first_transaction.amount, inputs])
    node.current_NBCs.append([first_transaction.amount, inputs])
    for i in range(1,N):
        node.NBCs.append([0,[]])
    for i in range(1,N):
        node.current_NBCs.append([0,[]])
    # node.current_NBCs = node.NBCs
    app.run(host='127.0.0.1', port=port, debug=True, use_reloader=False)
