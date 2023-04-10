import os
import sys

# Get the file name from the argument
try:
    file = sys.argv[1]
    command = sys.argv[1:]
except IndexError:
    print("Please provide the file name as an argument.")
    sys.exit(1)

# Open the file and read each line
try:
    with open(file) as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"{file} not found.")
    sys.exit(1)

# Create a dictionary to hold the IP addresses and port number
ip_and_port = {}

# Iterate through each line
for line in lines:
    # Split the line into IP and port
    ip, port = line.strip().split(':')
    # Add the IP to the dictionary, using the port number as the key
    if port in ip_and_port:
        ip_and_port[port].append(ip)
    else:
        ip_and_port[port] = [ip]

# Iterate through the dictionary, performing the nmap scan for each port
for port, ips in ip_and_port.items():
    # Perform the nmap scan on all IPs and port
    os.system(f"{command} {port} {' '.join(ips)}")
