import dpkt
import sys
import socket 
import getopt
import binascii
import collections
from dpkt.compat import compat_ord

def inet_to_str(inet):
    try:
        return socket.inet_ntop(socket.AF_INET, inet)
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)

def mac_addr(address):
	return ':'.join('%02x' % compat_ord(b) for b in address)