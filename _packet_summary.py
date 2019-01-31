import sys
import dpkt
from datetime import datetime

def tc (ts) :
    return datetime.utcfromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')

f_packet = open(sys.argv[1], 'rb')
pcap_file = dpkt.pcap.Reader(f_packet)


packet = 0
ip_packet = 0 
tcp_packet = 0
udp_packet = 0
arp_packet = 0
tstart = 0
tend = 0 

print("...SCANNING PACKAGE...")
for ts, buf in pcap_file:
    if tstart == 0 : 
        tstart = ts 
    tend = ts    
    try: 
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        trans = ip.data
        packet += 1

        # IPV4 IPV6 eth.type == dpkt.ethernet.ETH_TYPE_IP6 
        if eth.type == dpkt.ethernet.ETH_TYPE_IP or eth.type == dpkt.ethernet.ETH_TYPE_IP6 :
            ip_packet += 1
            if ip.p == dpkt.ip.IP_PROTO_UDP : 
                udp_packet += 1 
            if ip.p == dpkt.ip.IP_PROTO_TCP :
                tcp_packet += 1 
        elif eth.type == dpkt.ethernet.ETH_TYPE_ARP :
            arp_packet += 1

    except:
        tend = ts 
        print(sys.exc_info())
        break

fw = open('result/summary/summary.txt','a+') 
fw.write("{}\n".format(sys.argv[1]))
fw.write("packet : {}\n".format(packet))
fw.write("ip : {}\n".format(ip_packet))
fw.write("udp : {}\n".format(udp_packet))
fw.write("tcp : {}\n".format(tcp_packet))
fw.write("arp : {}\n".format(arp_packet))
fw.write("tstart : {}\n".format(tc(tstart)))
fw.write("tend : {}\n".format(tc(tend)))
fw.close()
f_packet.close()