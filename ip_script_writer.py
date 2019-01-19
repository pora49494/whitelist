import json
import sys

opcode = sys.argv[2]
filename = sys.argv[1].split(".")[0].split("/")[1]

with open('result/{}/ip_whitelist_{}.json'.format(filename,opcode), 'rb') as fp:
    devices_whitelist = json.load(fp)

fp.close()

fw_hard = open('result/{}/ip_iptables_hard_{}.sh'.format(filename,opcode), 'w')
fw_soft = open('result/{}/ip_iptables_soft_{}.sh'.format(filename,opcode), 'w')

fw_hard.write("#!/bin/sh\n")
fw_soft.write("#!/bin/sh\n")

# Installing NetfilterQueue
# fw.write("#Installing NetfilterQueue\n")
# fw.write("sudo apt-get install build-essential python-dev libnetfilter-queue-dev\n")

# Installing Python module
# fw.write("#Installing python module\n")
# fw.write("pip install NetfilterQueue\n")

# Add iptables script - clear old table
fw_hard.write("sudo iptables -F\n")
fw_soft.write("sudo iptables -F\n")

# Add iptables script - add new rules
for device_ip in devices_whitelist:
    wl = devices_whitelist[device_ip]["white_list"]
    for protocol in wl:
        for port in wl[protocol]:
            for ip in wl[protocol][port]["secured_ip"]:
                fw_hard.write("sudo iptables -A FORWARD -p {} --dport {} -d {} -s {} -j NFQUEUE --queue-num 1\n".format(protocol, port, device_ip, ip))
                fw_hard.write("sudo iptables -A FORWARD -p {} --dport {} -s {} -d {} -j NFQUEUE --queue-num 1\n".format(protocol, port, device_ip, ip))
                fw_soft.write("sudo iptables -A FORWARD -p {} -d {} -s {} -j NFQUEUE --queue-num 1\n".format(protocol, device_ip, ip))
                fw_soft.write("sudo iptables -A FORWARD -p {} -s {} -d {} -j NFQUEUE --queue-num 2\n".format(protocol, device_ip, ip))

for device_ip in devices_whitelist:
    fw_hard.write("sudo iptables -A FORWARD -d {} NFQUEUE --queue-num 1\n".format(device_ip))
    fw_hard.write("sudo iptables -A FORWARD -s {} NFQUEUE --queue-num 1\n".format(device_ip))
    fw_soft.write("sudo iptables -A FORWARD -d {} NFQUEUE --queue-num 1\n".format(device_ip))
    fw_soft.write("sudo iptables -A FORWARD -s {} NFQUEUE --queue-num 1\n".format(device_ip))

fw_hard.close()
fw_soft.close()