# coding_gpt_testing: a repo for getting GPT to create code and automatically test it. 
Here detail how to use all of the files together

To create the 1,475 queries, we leveraged LeetCode’s starter code for each problem, ensuring it was included in every query. Instead of inserting the code manually, we opted to automate this process. All files can be found in the folder scraping_code. 

First, we developed a script called curl.py to download the source code from each problem page. The script is executed by running python3 curl.py URL (where ‘URL’ is the link to the specific problem) from the command line.

To streamline the process further, we wrote another script, automate_curl.py, which utilizes the CSV file containing the LeetCode problem data. This allowed us to automatically generate all curl requests and save the responses as text files named question{question_number}.txt, with each file corresponding to its respective question number.

Next, we created a parser called extract.py to read each file and extract a dictionary entry for Python 3. To automate this step, we wrote automate_extract.py, which followed the same method as automate_curl.py. The parsed responses were saved as output_question{question_number}.txt, with each file corresponding to its respective question number.

Lastly, we needed to extract the response from the parser code out of a JSON object. To do this, we developed automate_parsed.py, which parsed through all the files and stored the results in extracted{question_number}.txt, with each file corresponding to its respective question number. We provided an example of Question 2 from LeetCode in the scraping_code folder. 


The original dataset of problems is obtained from https://www.kaggle.com/datasets/gzipchrist/leetcode-problem-dataset/code 
