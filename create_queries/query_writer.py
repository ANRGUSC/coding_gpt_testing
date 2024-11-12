import csv
import json
import os

csv_file = "leetcode_dataset - lc.csv"

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for row in reader:
        question_number = row[0]
        difficulty = row[4]
        question = row[2]

        if difficulty.lower() == "medium":
            file_name = f"query{question_number}.txt"
            extracted_file_name = f"extracted{question_number}.txt"

            # Check if the extracted file exists
            if not os.path.exists(extracted_file_name):
                print(f"Skipped {question_number} as the extracted file doesn't exist")
                continue

            # Read the content to insert from the extracted file
            with open(extracted_file_name, "r") as extracted_file:
                extracted_content = extracted_file.read()

            # Construct the file content with the extracted content
            file_content = f"""Write a python program to do the following, and put this program in a json object as the value corresponding to the key 'code'.
{question}
Write code that fits the following template: The program should continue below the following lines:
{extracted_content}"""

            with open(file_name, "w") as output_file:
                output_file.write(file_content)

print("Files generated successfully.")