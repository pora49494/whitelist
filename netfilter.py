from netfilterqueue import NetfilterQueue                                                                                        

accept_device_packet = []
accept_host_packet = []
drop_device_packet = []
drop_host_packet = [] 

def accept1 (pkt):
    accept_host_packet.append(pkt)
    pkt.accept()
     
def accept2 (pkt):
    accept_device_packet.append(pkt)
    pkt.accept()

def drop3 (pkt):
    drop_host_packet.append(pkt)
    pkt.accept()

def drop4 (pkt):
    drop_device_packet.append(pkt)
    pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, accept1)
nfqueue.bind(2, accept2)
nfqueue.bind(3, drop3)
nfqueue.bind(4, drop4)

try:
    nfqueue.run()
except KeyboardInterrupt:
    fw1 = open("AH1_data.txt", 'w')
    fw2 = open("AD2_data.txt", 'w')
    fw3 = open("DH3_data.txt", 'w')
    fw4 = open("DD4_data.txt", 'w')

    fw1.write(accept_host_packet)
    fw2.write(accept_device_packet)
    fw3.write(drop_host_packet)
    fw4.write(drop_device_packet)
    
    nfqueue.unbind()
                                  