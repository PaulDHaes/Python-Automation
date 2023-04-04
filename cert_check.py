#!/usr/bin/python3

import re
import sys

#check if cert is expired.
#.nmap file was executed with nmap --script ssl-cert,ssl-enum-ciphers arguments
def check_exp (ssl_list):
    with open(ssl_list, 'r') as file:
        nmap_output = file.read()

    for line in nmap_output.split('\n'):
        if 'Nmap scan report for' in line:
            ip = line.split()[-1]
        elif 'Not valid after: ' in line:
            ssl_cert = line
            #print(line)
            expiry_date = re.search(r'Not valid after:  (\S+)', ssl_cert)
            if expiry_date:
                expiry_date = expiry_date.group(1)
                if expiry_date < '2023-04-03':
                    print(f"The certificate for {ip} has expired on {expiry_date}")
                #else:
                    #print(f"The certificate for {ip} will expire on {expiry_date}")
            else:
                print(f"No expiry date found for {ip}")

#main function
def main():
    ssl_list = sys.argv[1]
    if len(sys.argv) != 2:
         print ('give me a .nmap file')
    check_exp(ssl_list)

#main
if __name__ == '__main__':
    main()