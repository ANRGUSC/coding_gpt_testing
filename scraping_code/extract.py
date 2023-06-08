import re
import sys

def extract_code(filename):
    with open(filename, 'r') as file:
        # Read the content of the file
        content = file.read()

        # Use regular expression to find the pattern
        pattern = re.compile(r'\{"lang":"Python3".*?\}', re.DOTALL)
        matches = pattern.findall(content)

        # Print the matches
        for match in matches:
            print(match)

# Check if filename is provided
if len(sys.argv) != 2:
    print("Usage: python3 extract_code.py <filename>")
    sys.exit(1)

# Extract the code
extract_code(sys.argv[1])

