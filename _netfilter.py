from netfilterqueue import NetfilterQueue
from kamene.all import * 
import os
import sys

def formatter(pkt) :
    payload = pkt.get_payload()
    
    packet_ip = IP(payload)
    proto = packet_ip.proto
    src_ip = packet_ip.src
    dst_ip = packet_ip.dst
    
    eth = Ether(payload)
    src_mac = eth.src
    dst_mac = eth.dst 

    udp = UDP(payload)
    sport = udp.sport
    dport = udp.dport 

    # proto,src_ip,src_mac,sport,dst_ip,dst_mac,dport
    result =  "{},{},{},{},{},{},{}".format(proto,src_ip,src_mac,sport,dst_ip,dst_mac,dport) 
    pkt.drop()

if __name__ == "__main__": 
    nf = NetfilterQueue()
    nf.bind(1, formatter)
    try :
        fw = open("result\drop.txt","a+")
    except :
        fw = open("result\drop.txt","w")

    try:
        nf.run()    
    except KeyboardInterrupt:
        nf.unbind()