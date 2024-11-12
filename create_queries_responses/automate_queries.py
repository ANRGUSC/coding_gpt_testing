import os
import subprocess

# Get the list of files in the current directory
files = os.listdir()

# Iterate over the files and run get_Code.py for each query file
for file in files:
    if file.startswith("query") and file.endswith(".txt"):
        command = f'python3 get_Code.py {file}'
        subprocess.run(command, shell=True)
