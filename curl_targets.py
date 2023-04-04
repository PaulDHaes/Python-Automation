#!/usr/bin/python3
import argparse
import subprocess
import os

#arguments helper
parser = argparse.ArgumentParser()
parser.add_argument("-f", help="file containing IP's")
args = parser.parse_args()

# open file and read IP's into a list
ip_file = args.f
ip_list = []

with open(ip_file, 'r') as f:
    for line in f:
        ip_list.append(line)

# for each IP in the list, run a curl command and print the response body
for ip in ip_list:
    print("\n")
    print ("running curl for {0}".format(ip))
    try:
        print(os.system('curl --insecure -s "https://'+ip.rstrip()+'/special/path"'))
    except:
        print ("error")