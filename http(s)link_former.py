import re

def add_protocol(ip_port):
    ip, port = ip_port.split(':')
    if port in ('443', '631', '664', '832', '1129', '1184', '2381', '4036', '4849', '5443', '5989', '5990', '6443', '6771', '7202', '7443', '7677', '8243', '8443', '8089','8991', '9295', '9443', '9444', '16993', '20003'):
        return f'https://{ip}:{port}'
    else:
        return f'http://{ip}:{port}'

filename = 'test.txt' # change this to the name of your file
output_filename = 'output_ip.txt' # change this to the name of the output file

with open(filename, 'r') as f:
    lines = f.readlines()

output_lines = []
for line in lines:
    ip_port = line.strip()
    output_lines.append(add_protocol(ip_port))

with open(output_filename, 'w') as f:
    f.writelines('\n'.join(output_lines))
