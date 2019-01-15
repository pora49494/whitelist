import subprocess as subprocess 

def get_dns (ip) :
  dns = list()
  command = "dig +noall +answer -x {}".format(ip)
  dns_records = str(subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()).split("\\n")
  for index in range(0,len(dns_records)-1) :
    dns.append(dns_records[index].split("\\t")[-1]) 
  
  return dns