import csv
import json

csv_file = "leetcode_dataset - lc.csv"

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for row in reader:
        question_number = row[0]
        difficulty = row[4]
        question = row[2]

        if difficulty.lower() == "hard":
            file_name = f"query{question_number}.txt"
            file_content = f"Write a python program to do the following, and put this program in a json object as the value corresponding to the key 'code'.\n{question}"

            with open(file_name, "w") as output_file:
                output_file.write(file_content)

print("Files generated successfully.")