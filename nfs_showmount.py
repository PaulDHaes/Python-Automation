#!/usr/bin/python3
import os
import sys

#execute command
def showmount(ip):
    print("\n")
    response = os.system("showmount -e " + ip)

#read_file
def read_file(filename):
    with open(filename) as f:
        for line in f:
            ip = line.strip()
            showmount(ip)

#main function
def main():
    nfs_list = sys.argv[1]
    if len(sys.argv) != 2:
         print ('give list of IP addresses')
    read_file(nfs_list)

#main
if __name__ == '__main__':
    main()