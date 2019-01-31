import sys
import json
import socket

filename = sys.argv[1]

with open(filename, 'r') as fp:
    devices_profile = json.load(fp)

counter = 1 
for device in devices_profile :
    ip = device 
    mac = devices_profile[device]["mac_address"]
    wl = devices_profile[device]["white_list"]
    udp = devices_profile[device]["white_list"]["udp"]
    tcp = devices_profile[device]["white_list"]["tcp"]
    
    print ("ID : {}".format(counter))
    print ("IP Address  : {}".format(ip))
    print ("MAC Address : {}".format(mac))
    if (len(udp) + len(tcp)) > 0 :  
        print ("-"*100)
        print ("IP Address".ljust(20,' '), end = "")
        print ("Port/Protocol".ljust(30,' '), end = "")
        print ("SECURE".ljust(15,' '), end = "")
        print ("ALL".ljust(15,' '), end = "")
        print ("RATIO".ljust(20,' '))

    for port in udp : 
        hosts = udp[port]["hosts"]
        for host_ip in hosts : 
            ratio = hosts[host_ip]["secure_ratio"] 
            secure = hosts[host_ip]["servers_secure_record"] 
            record = hosts[host_ip]["servers_record"] 
            print ("{}".format(host_ip).ljust(20,' '), end = "")
            try :
                print ("{}({})/UDP".format(socket.getservbyport(int(port)),port).ljust(30,' '), end = "")
            except :
                print ("{}/UDP".format(port).ljust(30,' '), end="")
            print ("{}".format(secure).ljust(15,' '), end = "")
            print ("{}".format(record).ljust(15,' '), end = "")
            print ("{}".format(ratio).ljust(20,' ')) 
      
    for port in tcp : 
        hosts = tcp[port]["hosts"] 
        for host_ip in hosts : 
            ratio = hosts[host_ip]["secure_ratio"] 
            secure = hosts[host_ip]["servers_secure_record"] 
            record = hosts[host_ip]["servers_record"] 
            print ("{}".format(host_ip).ljust(20,' '), end = "")
            try :
                print ("{}({})/TCP".format(socket.getservbyport(int(port)),port).ljust(30,' '), end = "")
            except :
                print ("{}/TCP".format(port).ljust(30,' '), end="")
            print ("{}".format(secure).ljust(15,' '), end = "")
            print ("{}".format(record).ljust(15,' '), end = "")
            print ("{}".format(ratio).ljust(20,' ')) 
    
    print ("="*100)
    counter += 1      
