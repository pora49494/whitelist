import networkx as nx 
from matplotlib import pyplot as plt 
import sys
import json

G = nx.Graph()
switch_ip = "0"
prefix = str()
color = []

filename = sys.argv[1].split(".")[0].split("/")[1]
opcode = str(sys.argv[2])

with open('result/{}/ip_devices_{}.json'.format(filename,opcode), 'r') as fp:
    devices = json.load(fp)

for ip in devices : 
    if ip.split(".")[3] == '1' :
        switch_ip = ip
        prefix = ".".join(ip.split(".")[0:3])
        print(prefix)

if switch_ip != '0' :
    for ip in devices : 
        if ip == switch_ip :
            continue
        if prefix == ".".join(ip.split(".")[0:3]) :
            G.add_edge(switch_ip,'.'+ip.split('.')[3])
        else :
            G.add_node(ip)
else : 
    if len(devices) == 1 : 
        for ip in devices : 
            key = ip 
        G.add_node(key)
    else :
        for ip in devices : 
            G.add_edge(' ',ip)

plt.figure(1,figsize=(4,4))
nx.draw(G, with_labels=True,node_color='0.85', node_size = 3000,font_size=20)
plt.savefig('result/{}/graph_ip_devices_{}.png'.format(filename,opcode))