import requests
import time
host='127.0.0.1'
port=5000
baseurl = 'http://{}:{}/'.format(host, port)
N = 5

for n in range(N):
    load = {'public_key':port + n + 1}
    r = requests.post(baseurl + "nodes/register", json = load)
    rejson = r.json()
    myid = rejson["nodeCount"]
    print("I am node number {} and my unique id is {}!".format(n, myid))
