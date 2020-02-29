import requests
import time
from node import Node
host='127.0.0.1'
ips = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5'] # okeanos
port=5000
baseurl = 'http://{}:{}/'.format(host, port)
N = 3

# id = 0: bootstrap node
for n in range(1, N):
    node = Node()

    # send public_key to bootstrap
    # request id from bootstrap node
    public_key = node.wallet.public_key
    load = {'public_key': str(public_key) }
    r = requests.post(baseurl + "nodes/register", json = load)
    if(not r.status_code == 200):
        print(r.text)
        exit(1)
    rejson = r.json()
    myid = rejson["id"]
    bootstrap_public_key = rejson["bootstrap_public_key"]
    node.id = myid

    print("I am node number {} from file addNodes1.py and my unique id is {}!".format(n, node.id))
