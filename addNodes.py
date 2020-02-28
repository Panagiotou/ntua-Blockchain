import requests
import time
from node import Node
host='127.0.0.1'
ips = [192.168.1.1, 192.168.1.2, 192.168.1.3, 192.168.1.4, 192.168.1.5] # okeanos
port=5000
baseurl = 'http://{}:{}/'.format(host, port)
N = 5

# id = 0: bootstrap node
for n in range(1, N):
    node = Node()

    # send public_key to bootstrap
    # request id from bootstrap node
    public_key = node.wallet.public_key
    load = {'public_key': str(public_key) }
    r = requests.post(baseurl + "nodes/register", json = load)
    rejson = r.json()
    myid = rejson["nodeCount"]
    print("I am node number {} and my unique id is {}!".format(n, myid))
    node.id = myid

    # transaction
    amount = 100
    transaction = node.create_transaction(bootstrap_public_key, bootstrap_private_key, public_key, amount)
    # add transaction to a block
    block.listOfTransactions.append(transaction)
