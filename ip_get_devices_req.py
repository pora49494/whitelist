import getopt
import dpkt
import sys
import os 
import json

from functions.address_translator import inet_to_str, mac_addr 
from functions.ip_dns_translator import get_dns

# Devices profile [key:mac]
devices_profile = {}

filename = sys.argv[1].split(".")[0].split("/")[1]
f_device = open(sys.argv[1], 'rb')
pcap_file = dpkt.pcap.Reader(f_device)

profile = dict()

# Find device in LAN 
print("...FINDING DEVICES...")
for ts, buf in pcap_file:

    eth = dpkt.ethernet.Ethernet(buf)
    if eth.type == dpkt.ethernet.ETH_TYPE_ARP :
        
        if eth.arp.op != dpkt.arp.ARP_OP_REQUEST : 
            pass 

        arp = eth.arp
        mac_target = mac_addr(arp.tha).strip() 
        mac_source = mac_addr(arp.sha).strip()
        ip_target = inet_to_str(arp.tpa).strip()
        ip_source = inet_to_str(arp.spa).strip()

        if ip_source not in devices_profile and mac_target == '00:00:00:00:00:00' : 
            devices_profile[ip_source] = { 
            	"mac_address" : [],
            	"white_list" : {'udp' : dict(), 'tcp' : dict(),}
            }
        if mac_target == '00:00:00:00:00:00' and mac_source not in devices_profile[ip_source]["mac_address"]:
            devices_profile[ip_source]["mac_address"].append(mac_source)

with open('result/{}/ip_devices_req.json'.format(filename), 'w') as fp:
    json.dump(devices_profile, fp)

print("...DEVICES PROFILE SAVED...")

f_device.close()