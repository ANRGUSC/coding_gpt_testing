import requests
import sys

def download_source_code(url, output_file=None):
    try:
        # Send a HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # If output_file is specified, save content to the file
            if output_file:
                with open(output_file, 'w') as file:
                    file.write(response.text)
                print(f"Source code downloaded and saved as {output_file}")
            # Otherwise, print the content to stdout
            else:
                print(response.text)
        else:
            print(f"Error: Unable to retrieve the source code (HTTP {response.status_code})")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Check if URL is provided
if len(sys.argv) < 2:
    print("Usage: python3 download_source_code.py <URL> [output_file]")
    sys.exit(1)

# Download the source code
download_source_code(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)

