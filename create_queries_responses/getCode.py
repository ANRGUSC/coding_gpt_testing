import requests
import json
import re
import sys


def query_gpt3(query, tokens=1000):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": query}],
        "temperature": 0.7
    }

    response = requests.post(ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        raise Exception(f"Error querying GPT-3 API: {response.status_code} - {response.text}")

def write_string_to_file(string, filename):
    with open(filename, 'w') as file:
        file.write(string)

if __name__ == "__main__":
    ENDPOINT = "https://api.openai.com/v1/chat/completions"

    with open('api_key.txt', 'r') as file:
    # Read the API key from the file as a string
        API_KEY = file.read().strip()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    # Read the query file as a string
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        query = file.read().strip()


    rawresponse = query_gpt3(query)
    #print("Raw response: ", rawresponse)

    response = rawresponse['choices'][0]['message']['content']
    print(f"GPT-3 Response: {response}")
    print(type(response))

    result = json.loads(response)['code']

    if result:
        print("The extracted text between the quotes is:\n\n" + result)
        write_string_to_file(result, 'code_'+filename[:len(filename)-4]+'.py')
    else:
        print("No text found between the specified quotes.")
