# coding_gpt_testing: a repo for getting GPT to create code and automatically test it. 
Here detail how to use all of the files together

To create the 1,475 queries, we leveraged LeetCode’s starter code for each problem, ensuring it was included in every query. Instead of inserting the code manually, we opted to automate this process. All relevant files can be found in the scraping_code folder.

First, we developed a script called curl.py to download the source code from each problem page. The script is executed by running python3 curl.py URL (where ‘URL’ is the link to the specific problem) from the command line. To streamline the process further, we wrote another script, automate_curl.py, which utilizes a CSV file containing the LeetCode dataset we used. This allowed us to automatically generate all curl requests and save the responses as text files named question{question_number}.txt, with each file corresponding to its respective question number.

Next, we created a parser called extract.py to read each file and extract a dictionary entry for Python 3. To automate this step, we wrote automate_extract.py, which followed the same method as automate_curl.py. The parsed responses were saved as output_question{question_number}.txt, with each file corresponding to its respective question number.

To process the parsed data (now in a JSON object), we developed automate_parsed.py, which extracted the JSON object response into the starter code we wanted to insert into every query. This script parsed through all the files and saved the results in extracted{question_number}.txt, with each file corresponding to its respective question number. An example of Question 2 from LeetCode is provided in the scraping_code folder.

Once the starter code was prepared, we were ready to write all the queries. All files/scripts used to write the queries are stored in the create_queries_responses folder. We wrote a program called query_writer.py to create the queries using the LeetCode CSV file and the extracted starter code files. Each query were saved as query{question_number}.txt, with each file corresponding to its respective question number. A sample query, query2.txt, is provided in the queries folder. Note: To generate all queries, you must edit the script query_wrtier.py to specify the difficulty level (“easy,” “medium,” or “hard”).

Finally, to generate responses using ChatGPT’s GPT-3.5-turbo, we wrote getCode.py, which uses an API key to access ChatGPT. To change the model of testing, you can specify which model you want in the script. We automated this step using automate_queries.py to run all queries simultaneously, storing the responses in code_query{question_number}.py, with each file corresponding to its respective question number. A sample output can be found in the folder ouput_code. 

When we returned to Chain of Thought (CoT) prompt engineering, you can find an example query in CoTquery.txt. Additionally, when we incorporated failed test cases, an example query is available in the folder queries called IncorporatingFailedQuery.txt.

The original dataset of problems is obtained from https://www.kaggle.com/datasets/gzipchrist/leetcode-problem-dataset/code 
