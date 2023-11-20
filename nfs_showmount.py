#!/usr/bin/python3
import os
import sys
import socket

# execute command
def showmount(ip):
    print("\n")
    response = os.system("showmount -e " + ip)

# read_file
def read_file(filename):
    with open(filename) as f:
        for line in f:
            ip = line.strip()
            try:
                with socket.create_connection((ip, 111), timeout=5):
                    showmount(ip)
            except socket.timeout:
                print(f"Connection to {ip} timed out after 5 seconds. Moving on to the next IP.")
            except Exception as e:
                print(f"Error connecting to {ip}: {e}")

# main function
def main():
    nfs_list = sys.argv[1]
    if len(sys.argv) != 2:
         print ('give list of IP addresses')
    read_file(nfs_list)

# main
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Program stopped by user.")
