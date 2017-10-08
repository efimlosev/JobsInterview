#!/usr/bin/python
import argparse,re
pattern_ip = '^(\d{1,3}\.){0,3}\d{1,3}$'
pattern_cidr = '^(\d{1,3}\.){0,3}\d{1,3}/\d{1,2}$'

def Main ():
    parser = argparse.ArgumentParser(usage = './dockler.py 192.168.0.1 192.168.0.0/24' )
    parser.add_argument('ip',  help='Give me an IP', type=str) 
    parser.add_argument('cidr',  help='Give me a CIDR', type=str)
    args = parser.parse_args()
    print test_ip_in_range(args.ip,args.cidr)
def test_ip_in_range(ip_to_check, subnet_with_mask):

    byte_to_bits = lambda b: bin(int(b))[2:].rjust(8, '0')
    ip_to_bits = lambda ip: ''.join([byte_to_bits(b) for b in ip.split('.')])

    if re.match(pattern_ip, ip_to_check) and re.match(pattern_cidr, subnet_with_mask):
        
        ip_to_check_ip_bits = ip_to_bits(ip_to_check)
        subnet_without_mask,snet_mask = subnet_with_mask.split('/')
        subnet_without_mask_ip_bits = ip_to_bits(subnet_without_mask)
  
        if subnet_without_mask_ip_bits[:int(snet_mask)] == ip_to_check_ip_bits [:int(snet_mask)]:
            return "OK"
        else:
            return "NOT OK"
    

    else:
        raise ValueError("INPUT Error")
            

if __name__ == '__main__':

    Main()
