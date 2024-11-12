import csv
import json

# CSV file path
csv_file = "leetcode_dataset - lc.csv"

# Open the CSV file
with open(csv_file, "r") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        column_a_value = row[0]
        output_filename = f"output_question{column_a_value}.txt"
        extracted_filename = f"extracted{column_a_value}.txt"

        # Load the content from the output file
        with open(output_filename, "r") as output_file:
            output_content = output_file.read()

            # Parse the JSON string from the output content
            try:
                parsed_output = json.loads(output_content)
            except json.JSONDecodeError:
                print(f"Invalid JSON in {output_filename}")
                continue

            # Extract the code from the parsed JSON
            if "code" in parsed_output:
                code = parsed_output["code"]
            else:
                print(f"'code' key not found in {output_filename}")
                continue

            # Save the extracted code to a file
            with open(extracted_filename, "w") as extracted_file:
                extracted_file.write(code)