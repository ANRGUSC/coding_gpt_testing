import csv
import subprocess

csv_filename = "leetcode_dataset - lc.csv"
extract_script = "extract.py"

# Open the CSV file
with open(csv_filename, "r") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        column_a_value = row[0]  # Assuming Column A is the first column

        # Run the extract.py command for each line
        command = ["python3", extract_script, f"question{column_a_value}.txt"]
        subprocess.run(command)