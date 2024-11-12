import csv
import subprocess

csv_file = "leetcode_dataset - lc.csv"

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    
    # Iterate over each row in the CSV file
    for row in reader:
        leet_code_link = row[8]
        question_number = row[0]
        
        # Construct the command
        command = f"python3 curl.py {leet_code_link} > question{question_number}.txt"
        
        # Run the command using subprocess
        subprocess.run(command, shell=True)