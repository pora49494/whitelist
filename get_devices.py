import getopt
import dpkt
import sys
import os 
import json

from functions.address_translator import inet_to_str, mac_addr 
from functions.ip_dns_translator import get_dns

# Devices profile [key:mac]
devices_profile = {}

f_device = open(sys.argv[1], 'rb')
pcap_file = dpkt.pcap.Reader(f_device)

# Find device in LAN 
print("...FINDING DEVICES...")
for ts, buf in pcap_file:

    eth = dpkt.ethernet.Ethernet(buf)
    if eth.type == dpkt.ethernet.ETH_TYPE_ARP :
        arp = eth.arp

        mac_target = mac_addr(arp.tha).strip() 
        mac_source = mac_addr(arp.sha).strip()

        if mac_target not in devices_profile and mac_target != '00:00:00:00:00:00' : 
            devices_profile[mac_target] = { 
            	"mac_address" : mac_target,
            	"ip_address" : inet_to_str(arp.tpa),
            	"white_list" : {'udp' : dict(), 'tcp' : dict(),}
            }

        if mac_source not in devices_profile and mac_source != '00:00:00:00:00:00' : 
        	devices_profile[mac_source] = { 
            	"mac_address" : mac_source,
            	"ip_address" : inet_to_str(arp.spa),
            	"white_list" : {'udp' : dict(), 'tcp' : dict(),}
            }

with open('devices.json', 'w') as fp:
    json.dump(devices_profile, fp)

print("...DEVICES PROFILE SAVED...")

f_device.close()