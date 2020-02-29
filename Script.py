import os, sys

host='127.0.0.1'
N = 4
ips = []
for i in range(N):
    ips.append(host[:-1] + str(i + 2))

for ip in ips:
    os.system("gnome-terminal -e \"python3 Rest.py {}\"".format(ip))
