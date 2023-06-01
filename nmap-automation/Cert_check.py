import os
import sys
import datetime

def parse_certificate_dates(output):
    lines = output.split('\n')
    start_date_str = None
    end_date_str = None

    for line in lines:
        if "Not valid before:" in line:
            start_date_str = line.split(": ")[1].strip()
        elif "Not valid after:" in line:
            end_date_str = line.split(": ")[1].strip()

    return start_date_str, end_date_str

def check_certificate_validity(ip, port):
    command = f"nmap --script ssl-cert -p {port} {ip}"
    result = os.popen(command).read()

    if "Certificate expired" in result or "Certificate not yet valid" in result:
        return False

    start_date_str, end_date_str = parse_certificate_dates(result)

    if start_date_str is None or end_date_str is None:
        return False

    # Update the datetime format based on the new certificate date format
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%dT%H:%M:%S")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%dT%H:%M:%S")
    current_time = datetime.datetime.now()

    if start_date <= current_time <= end_date:
        return True
    else:
        print(f"Certificate expired on: {end_date}")
        return False

def main(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                ip, port = line.split(':')
                if check_certificate_validity(ip, port):
                    print(f"Certificate is valid: {ip}:{port}")
                else:
                    print(f"Certificate is invalid: {ip}:{port}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
