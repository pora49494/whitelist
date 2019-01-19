import getopt
import dpkt
import sys
import os 
import json

from functions.address_translator import inet_to_str, mac_addr 
from functions.ip_dns_translator import get_dns

# Constant 
PACKET_TRES = 1000000
GROUP_TIME_LENGTH = 60

# Check number of packets
packets_counter = 0
 
# Server profile  {DNS : IP}
servers_profile = dict() 

# Status of server in time (T)
servers_status = dict()
# - [SS] is decided based on first packet
# |- [SS] is True  : first packet is from device
# |- [SS] is False : otherwise 

# Record how many time [SS] is show up 
servers_record = dict()

# Record how many time [SS] is True
servers_secure_record = dict()

group_time_length = -GROUP_TIME_LENGTH - 1 

def check_device_side ( src, dst ):
    if src in devices_profile : 
        return 'src' 
    elif dst in devices_profile :
        return 'dst' 
    return None 

# Open file 

filename = sys.argv[1].split(".")[0].split("/")[1]
f_package = open("data/{}".format(sys.argv[1]), 'rb')
pcap_file = dpkt.pcap.Reader(f_package)
opcode = str(sys.argv[2])

with open('mac_devices_{}.json'.format(opcode), 'r') as fp:
    devices_profile = json.load(fp)


print("...SCANNING PACKAGE...")
for ts, buf in pcap_file:

    # Check within group
    if ts - group_time_length > GROUP_TIME_LENGTH :
        group_time_length = ts 
        # protocol device server
        for ppds in servers_status : 
            # Create data status 
            if ppds not in servers_record :
                servers_record[ppds] = 1
                servers_secure_record[ppds] = 0         
            # Server profile 
            if servers_status[ppds] :
                servers_secure_record[ppds] += 1  
            servers_record[ppds] += 1

        servers_status = dict()
        
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
            
            device_side = check_device_side(src_mac, dst_mac)
            # PPDS : Protocol | Port | Device's IP | Server's IP
            if device_side == 'src' : 
                ppds = "{}-{}-{}-{}".format(protocol, port, src_mac, dst_ip)
                if ppds not in servers_status : 
                    servers_status[ppds] = True 

            elif device_side == 'dst' : 
                ppds = "{}-{}-{}-{}".format(protocol, port, dst_mac, src_ip)
                if ppds not in servers_status : 
                    servers_status[ppds] = False 

    except:
        print(sys.exc_info())
        break


for ppds in servers_record : 
    # Ratio of secure record is over 0.90 : Secured
    secure_ratio = servers_secure_record[ppds] / servers_record[ppds]
    if secure_ratio > 0.90 : 
        protocol, port, device_mac, server_ip = ppds.split("-")   
        wl = devices_profile[device_mac]["white_list"]
        # Check if this protocol is already existed in this device_profile
        if port not in wl[protocol] : 
            wl[protocol][port] = {
                'secured_ip' : list(),
                'hosts' : dict()
            } 

        # Append server dns if it is avaliable 
        wl[protocol][port]['hosts'][server_ip] = {
            "secure_ratio" : secure_ratio,
            "servers_secure_record" : servers_secure_record[ppds],
            "servers_record" : servers_record[ppds],
        }

        # Add server's dns to device' WL
        if server_ip not in wl[protocol][port]['secured_ip'] : 
             wl[protocol][port]['secured_ip'].append(server_ip)

with open('result/{}/mac_whitelist_{}.json'.format(filename,opcode), 'w') as fp:
    content = json.JSONEncoder().encode(devices_profile)
    fp.write(content)

f_package.close()