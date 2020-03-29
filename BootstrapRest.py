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
from copy import deepcopy
PRINTCHAIN = False
# CLIENT = 1                                  # read transactions from noobcash client
CLIENT = 0                                # read transactions from txt



### JUST A BASIC EXAMPLE OF A REST API WITH FLASK
def read_transaction():
    if (CLIENT):
        print("******** Welcome to Noobcash Client . . . ********")
        while(True):
            input1 = input()
            if input1 == "view":
                node.chain.view()
            elif input1 == "balance":
                print("Wallet UTXO's: ", node.NBCs[node.id][0])
            elif input1 == "help":
                print("t <recipient_address> <amount>   New transaction: Sends to recipient_address wallet, amount NBC coins from wallet sender_address.")
                #Θα καλεί συνάρτηση create_transaction στο backend που θα υλοποιεί την παραπάνω λειτουργία.
                print("view                             View last transactions: Displays the transactions contained in the last validated block.")
                #Καλεί τη συνάρτηση view_transactions() στο backend που υλοποιεί την παραπάνω λειτουργία
                print("balance                          Show balance: Displays wallet UTXOs.")
            else:
                print("else")
                message = "'" + input1 + "'"
                a = input1.split()
                try:
                    int(a[2])
                    if(a[0] == 't'):
                        flag = 0
                        for r in node.ring:
                            if (r['ip'] == a[1]):
                                flag = 1
                                pk = r['public_key']
                                node.create_transaction(node.wallet.address, node.wallet.private_key, pk, int(a[2]))
                                break
                        if(flag == 0):
                            print("<recipient_address> invalid")
                    else:
                        print (message, "is not recognized as a command. Please type 'help' to see all the valid commands")
                except:
                    print (message, "except is not recognized as a command. Please type 'help' to see all the valid commands")
    else:
        # time.sleep(2)
        print("Reading input transactions from txt")
        f = open("5nodes_small/transactions" + str(node.id) + ".txt", "r")
        print(node.ring)
        for line in f:
            id, amount = (line).split()
            for n in node.ring:
                if int(n['id']) == int(id[-1]):
                    # time.sleep(1)
                    # print("LINE", line)
                    # start_new_thread(node.create_transaction, (node.wallet.address, node.wallet.private_key, n['public_key'], int(amount),))
                    node.create_transaction(node.wallet.address, node.wallet.private_key, n['public_key'], int(amount))
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
    # read_transaction()
    start_new_thread(read_transaction, ())

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

    block = jsonpickle.decode(data["block"])
    if(block.index > 0):
        valid = node.validate_block(block)

        if(valid):
            node.chain.add_block_to_chain(block)

            # node.previous_block = block
            # node.current_block = node.create_new_block(block.index + 1, block.currentHash_hex, 0, time.time(), block.difficulty, block.capacity)
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
        else:

            # start_new_thread(node.resolve_conflicts,())
            node.resolve_conflicts()
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
        node.add_transaction_to_block(transaction)

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
    BLOCK_CAPACITY = 5
    MINING_DIFFICULTY = 4
    N = 5  #Number of nodes i  the system

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
    genesis_block.add_transaction(first_transaction)
    blockchain.add_block_to_chain(genesis_block)
    node.chain = blockchain
    if(PRINTCHAIN): node.chain.printMe()
    # print("Genesis block, added to blockchain")
    # Create Second Block index is 2
    node.previous_block = None
    node.current_block = node.create_new_block(1, genesis_block.currentHash_hex, 0, time.time(), MINING_DIFFICULTY, BLOCK_CAPACITY)

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
