#!/bin/sh

python3 get_devices.py ./tcpdump-29-11-2018-4-12-2018.pcap
python3 find_whitelist.py ./tcpdump-29-11-2018-4-12-2018.pcap
python3 script_writer_hard.py 
chmod 777 iptables_script_hard.sh
iptables_script_hard 