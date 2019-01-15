import json

with open('devices_whitelist.json', 'rb') as fp:
    devices_whitelist = json.load(fp)

fp.close()

fw = open('iptables_script_soft.sh', 'w')

fw.write("#!/bin/sh\n")

# Installing NetfilterQueue
# fw.write("#Installing NetfilterQueue\n")
# fw.write("sudo apt-get install build-essential python-dev libnetfilter-queue-dev\n")

# Installing Python module
# fw.write("#Installing python module\n")
# fw.write("pip install NetfilterQueue\n")

# Add iptables script
for device_mac in devices_whitelist:
    wl = devices_whitelist[device_mac]["white_list"]
    for protocol in wl:
        for port in wl[protocol]:
            for ip in wl[protocol][port]["secured_ip"]:
                fw.write("sudo iptables -A FORWARD -p {} -m mac --mac-destination {} -s {} -j NFQUEUE --queue-num 1\n".format(protocol, device_mac, ip))
                fw.write("sudo iptables -A FORWARD -p {} -m mac --mac-source {} -d {} -j NFQUEUE --queue-num 2\n".format(protocol, device_mac, ip))

for device_mac in devices_whitelist:
    fw.write("sudo iptables -A FORWARD -m mac --destination {} NFQUEUE --queue-num 3\n".format(device_mac))
    fw.write("sudo iptables -A FORWARD -m mac --source {} NFQUEUE --queue-num 4\n".format(device_mac))

# --queue-num 1 : ACCEPT host -> device
# --queue-num 2 : ACCEPT device -> host 
# --queue-num 3 : DROP host -> device
# --queue-num 4 : DROP device -> host

fw.close()