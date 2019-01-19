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
    return "{},{},{},{},{},{},{}".format(proto,src_ip,src_mac,sport,dst_ip,dst_mac,dport) 

def accept1 (pkt):
    f = open("accept1.txt","w+")
    f.write("{}\n".format(formatter(pkt)))
    pkt.accept()
     
def accept2 (pkt):
    f = open("accept2.txt","w+")
    f.write("{}\n".format(formatter(pkt)))
    pkt.accept()

def drop3 (pkt):
    f = open("drop3.txt","w+")
    f.write("{}\n".format(formatter(pkt)))
    pkt.accept()

def drop4 (pkt):
    f = open("drop4.txt","w+")
    f.write("{}\n".format(formatter(pkt)))
    pkt.accept()

if __name__ == "__main__": 
    nf1 = NetfilterQueue()
    nf2 = NetfilterQueue()
    nf3 = NetfilterQueue()
    nf4 = NetfilterQueue()

    nf1.bind(1, accept1)
    nf2.bind(2, accept2)
    nf3.bind(3, drop3)
    nf4.bind(4, drop4)

    try:
        nf1.run()
        nf2.run()
        nf3.run()
        nf4.run()
    except KeyboardInterrupt:
        nf1.unbind()
        nf2.unbind()
        nf3.unbind()
        nf4.unbind()
                                  