import subprocess
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) < 3:
    print("Usage: python3 repeat-command.py input_file main_command [arg1 arg2 ...]")
    sys.exit(1)

input_file = sys.argv[1]
main_command = sys.argv[2]
additional_args = sys.argv[3:]

# Check if the input file exists
try:
    with open(input_file, 'r') as file:
        urls = file.read().splitlines()
except FileNotFoundError:
    print(f"Input file '{input_file}' not found.")
    sys.exit(1)

# Loop through each URL in the input file and execute the specified command
for url in urls:
    print(f"Command executing {main_command}{url}{additional_args}")

    # Construct the command by appending the URL and additional arguments
    command = [main_command, url] + additional_args
    
    # Execute the command
    try:
        print(f"{command}")
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

print("Script finished.")
