# Python script that automated boring taks related to Nmap

# Cert_check.py
Checks for if the certificate of the SSL/TLS is still valid.

## Example cert
Command to check cert nmap --script ssl-cert,ssl-enum-ciphers -p 443 google.com Amazon.com -oA cert
``` bash
Cert_check.py cert.nmap
```
### Output
if 1 or more certificates are outdated then it would output
"The certificate for 'IP' has expired on 'expiry_date'"
if no certificates are outdated then it would output 
"No expiry date found for 'IP'"

# nmap_script.py
Executes nmap command for all given ip with port syntax of file IP:PORT

## Example IP_PORT_list file

10.10.10.1:80
10.10.10.2:80
10.10.10.3:8080
10.10.10.4:8080
10.10.10.5:8081

## Example nmap_script
Example command 
``` bash
nmap_script.py IP_PORT_list.txt -sT -sV -v -n -Pn -v
```
What the script does it groups all ip's with the same port togheter and runs the command togheter
``` nmap
nmap -sT -sV -v -n -Pn -v -p Port_of_IP_PORT_list IP1_of_IP_PORT_list IP2_of_IP_PORT_list
```
### Output
normal nmap output of every port
80 -> 2 ip's
8080 -> 2 ip's
8081 -> 1 ip
