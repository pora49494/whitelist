#!/bin/sh
sudo iptables -F
sudo iptables -A FORWARD -p udp -d 133.11.168.53 -s 133.11.168.127 -j NFQUEUE --queue-num 1
sudo iptables -A FORWARD -p udp -s 133.11.168.53 -d 133.11.168.127 -j NFQUEUE --queue-num 2
sudo iptables -A FORWARD -p udp -d 133.11.168.53 -s 133.11.168.127 -j NFQUEUE --queue-num 1
sudo iptables -A FORWARD -p udp -s 133.11.168.53 -d 133.11.168.127 -j NFQUEUE --queue-num 2
sudo iptables -A FORWARD -p udp -d 133.11.168.70 -s 133.11.239.254 -j NFQUEUE --queue-num 1
sudo iptables -A FORWARD -p udp -s 133.11.168.70 -d 133.11.239.254 -j NFQUEUE --queue-num 2
sudo iptables -A FORWARD -p udp -d 133.11.168.70 -s 133.11.124.164 -j NFQUEUE --queue-num 1
sudo iptables -A FORWARD -p udp -s 133.11.168.70 -d 133.11.124.164 -j NFQUEUE --queue-num 2
sudo iptables -A FORWARD -p tcp -d 133.11.168.70 -s 133.11.168.38 -j NFQUEUE --queue-num 1
sudo iptables -A FORWARD -p tcp -s 133.11.168.70 -d 133.11.168.38 -j NFQUEUE --queue-num 2
sudo iptables -A FORWARD -p tcp -d 133.11.168.70 -s 72.246.189.24 -j NFQUEUE --queue-num 1
sudo iptables -A FORWARD -p tcp -s 133.11.168.70 -d 72.246.189.24 -j NFQUEUE --queue-num 2
sudo iptables -A FORWARD -p udp -d 133.11.168.11 -s 210.173.160.87 -j NFQUEUE --queue-num 1
sudo iptables -A FORWARD -p udp -s 133.11.168.11 -d 210.173.160.87 -j NFQUEUE --queue-num 2
sudo iptables -A FORWARD -p udp -d 133.11.168.11 -s 210.173.160.57 -j NFQUEUE --queue-num 1
sudo iptables -A FORWARD -p udp -s 133.11.168.11 -d 210.173.160.57 -j NFQUEUE --queue-num 2
sudo iptables -A FORWARD -p udp -d 133.11.168.11 -s 210.173.160.27 -j NFQUEUE --queue-num 1
sudo iptables -A FORWARD -p udp -s 133.11.168.11 -d 210.173.160.27 -j NFQUEUE --queue-num 2
sudo iptables -A FORWARD -p tcp -d 133.11.168.38 -s 133.11.168.70 -j NFQUEUE --queue-num 1
sudo iptables -A FORWARD -p tcp -s 133.11.168.38 -d 133.11.168.70 -j NFQUEUE --queue-num 2
sudo iptables -A FORWARD -d 133.11.168.1 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.1 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 192.168.0.120 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 192.168.0.120 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.53 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.53 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.70 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.70 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.11 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.11 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.50 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.50 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.60 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.60 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.82 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.82 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.84 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.84 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.52 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.52 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.30 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.30 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.37 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.37 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.25 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.25 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.6 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.6 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.38 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.38 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.26 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.26 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.110 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.110 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.97 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.97 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -d 133.11.168.111 NFQUEUE --queue-num 1
sudo iptables -A FORWARD -s 133.11.168.111 NFQUEUE --queue-num 1
