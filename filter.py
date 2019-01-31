import getopt
import dpkt
import sys
import os 
import json

from functions.address_translator import inet_to_str, mac_addr 
from functions.ip_dns_translator import get_dns
 
# Record how many time [SS] is show up 
record_drop_device = dict()
record_drop_host = dict()
record_drop_not_relate = dict()
record_accept = dict()

# Open file 
traffic = sys.argv[2]
filename = sys.argv[1]

with open(filename, 'rb') as fp:
    devices_whitelist = json.load(fp)
    
f_packet = open(sys.argv[2], 'rb')
pcap_file = dpkt.pcap.Reader(f_packet)

print("...SCANNING PACKAGE...")
for ts, buf in pcap_file:
      
    # Start Analysis
    try: 
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        trans = ip.data

        # IPV4 IPV6 eth.type == dpkt.ethernet.ETH_TYPE_IP6 
        if eth.type == dpkt.ethernet.ETH_TYPE_IP \
          and ( ip.p == dpkt.ip.IP_PROTO_UDP or ip.p == dpkt.ip.IP_PROTO_TCP ) : 
          
            protocol = "udp" if ip.p == dpkt.ip.IP_PROTO_UDP else "tcp" 
            port = str(min(trans.sport, trans.dport))
            src_ip = inet_to_str(ip.src).strip()
            dst_ip = inet_to_str(ip.dst).strip()
            src_mac = mac_addr(eth.src).strip() 
            dst_mac = mac_addr(eth.dst).strip() 
            key = "{}-{}-{}-{}".format(protocol, port, src_ip, dst_ip)
            
            if src_ip in devices_whitelist : 
                if port in devices_whitelist[src_ip]["white_list"][protocol] and dst_ip in devices_whitelist[src_ip]["white_list"][protocol][port]["secured_ip"] :
                    if key not in record_accept : 
                        record_accept[key] = 1 
                        continue 
                    record_accept[key] += 1      
                else : 
                    if key not in record_drop_device : 
                        record_drop_device[key] = 1
                        continue 
                    record_drop_device[key] += 1

            elif dst_ip in devices_whitelist : 
                if port in devices_whitelist[dst_ip]["white_list"][protocol] and src_ip in devices_whitelist[dst_ip]["white_list"][protocol][port]["secured_ip"] :
                    if key not in record_accept : 
                        record_accept[key] = 1 
                        continue 
                    record_accept[key] += 1
                else : 
                    if key not in record_drop_host : 
                        record_drop_host[key] = 1
                        continue 
                    record_drop_host[key] += 1

            else : 
                if key not in record_drop_not_relate :
                    record_drop_not_relate[key] = 1
                    continue
                record_drop_not_relate[key] += 1   
              
    except:
        print(sys.exc_info())
        continue

with open("result/filter/{}.json".format(traffic.split(".")[0].split('/')[1]), 'w') as fp:
    record = {
      'accept' : record_accept,
      'drop_device' : record_drop_device,
      'drop_host'  : record_drop_host,
      'drop_not_relate' : record_drop_not_relate 
    }
    content = json.JSONEncoder().encode(record)
    fp.write(content)

f_packet.close()