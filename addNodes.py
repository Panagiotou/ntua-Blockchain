import requests
import time
from node import Node
host='127.0.0.1'
port=5000
baseurl = 'http://{}:{}/'.format(host, port)
N = 5

for n in range(N):
    node = Node()
    public_key = node.wallet.public_key
    load = {'public_key': str(public_key) }
    r = requests.post(baseurl + "nodes/register", json = load)
    rejson = r.json()
    myid = rejson["nodeCount"]
    print("I am node number {} and my unique id is {}!".format(n, myid))
