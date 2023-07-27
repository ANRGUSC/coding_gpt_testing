from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Set up Chrome driver
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the LeetCode login page
driver.get('https://leetcode.com/accounts/login/')

# Find the username and password fields, and enter your credentials
username_field = driver.find_element(By.ID, 'id_login')
username_field.send_keys('minda-li')
password_field = driver.find_element(By.ID, 'id_password')
password_field.send_keys('Minda.li@12')

# Submit the login form
password_field.send_keys(Keys.RETURN)

time.sleep(30)

# Verify if login was successful
if driver.current_url == 'https://leetcode.com/':
    print('Login successful!')
else:
    print('Login failed.')

# Wait for the login process to complete
driver.implicitly_wait(10)

# Navigate to the LeetCode problem page
driver.get('https://leetcode.com/problems/reverse-integer/')


element = WebDriverWait(driver, 380).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#headlessui-listbox-button-\:r1k\:")))
#headlessui-listbox-button-\:r1j\:
#headlessui-listbox-button-\:r1k\:

# Find the language dropdown button
language_dropdown_button = driver.find_element(By.CSS_SELECTOR, '#headlessui-listbox-button-\:r1k\:')
#headlessui-listbox-button-\:r1l\:
# Click on the language dropdown button
language_dropdown_button.click()

# Find the Python3 option and click on it
python3_option = driver.find_element(By.CSS_SELECTOR, "#headlessui-listbox-option-\:r2a\:")
#headlessui-listbox-option-\:r29\:
#headlessui-listbox-option-\:r2u\:
#headlessui-listbox-option-\:r2a\: > div
#headlessui-listbox-option-\:r2b\:
#headlessui-listbox-option-\:r2a\:
#headlessui-listbox-option-\:r2v\:
python3_option.click()

time.sleep(40)

#div_element = driver.find_element((By.CSS_SELECTOR, '#editor > div.flex.flex-1.flex-col.overflow-hidden.pb-2.\[\&_\.scroll-decoration\]\:\!shadow-none > div.flex-1.overflow-hidden > div > div > div.overflow-guard > div.monaco-scrollable-element.editor-scrollable.vs.mac'))
#editor > div.flex.flex-1.flex-col.overflow-hidden > div.flex-1.overflow-hidden > div > div > div.overflow-guard
#editor > div.flex.flex-1.flex-col.overflow-hidden
#editor > div.flex.flex-1.flex-col.overflow-hidden.pb-2.\[\&_\.scroll-decoration\]\:\!shadow-none > div.flex-1.overflow-hidden > div > div > div.overflow-guard > div.monaco-scrollable-element.editor-scrollable.vs.mac > div.lines-content.monaco-editor-background > div.view-lines.monaco-mouse-cursor-text
#editor > div.flex.flex-1.flex-col.overflow-hidden.pb-2.\[\&_\.scroll-decoration\]\:\!shadow-none > div.flex-1.overflow-hidden > div > div > div.overflow-guard > div.monaco-scrollable-element.editor-scrollable.vs.mac
#editor > div.flex.flex-1.flex-col.overflow-hidden.pb-2.\[\&_\.scroll-decoration\]\:\!shadow-none > div.flex-1.overflow-hidden > div > div > div.overflow-guard > div.monaco-scrollable-element.editor-scrollable.vs.mac > div.lines-content.monaco-editor-background > div.view-lines.monaco-mouse-cursor-text

# Select the element using its class name.
elements = WebDriverWait(driver, 380).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".view-lines.monaco-mouse-cursor-text")))
print ('found you')
elements = driver.find_element(By.CSS_SELECTOR, '.view-lines.monaco-mouse-cursor-text')
print('worked')
#elements = WebDriverWait(driver, 380).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".view-lines.monaco-mouse-cursor-text")))
#driver.find_element(By.CSS_SELECTOR, ".view-lines.monaco-mouse-cursor-text")

# If you want to interact with the first element with class 'view-line' under the main div
# Get the first div from the elements
first_div = elements[0]

# Find the first 'view-line' within the first div
view_line = first_div.find_elements_by_class_name("view-line")

print('ready to click')

# Now interact with that 'view-line' 
view_line.click()

# Send some keys (this is similar to entering the text).
view_line.send_keys("Hello, World!")

# Click on the element to give it focus (if needed)
#div_element.click()

# Perform an action to trigger the file upload dialog
actions = ActionChains(driver)
#actions.move_to_element(div_element).click().perform()

# Add the path of the file you want to upload
file_path = '/Users/mindali/Research/All_Easy_Query/code_query7.py'
#div_element.send_keys(file_path)

# Find and click the "Submit" button
submit_button = driver.find_element(By.CSS_SELECTOR, "#qd-content > div.h-full.flex-col.ssg__qd-splitter-secondary-w > div > div:nth-child(3) > div > div > div > div > div.mx-4.my-\[10px\].flex.w-full > div.relative.ml-auto.flex.items-center.gap-3 > button.py-1\.5.font-medium.items-center.whitespace-nowrap.focus\:outline-none.inline-flex.text-label-r.bg-green-s.dark\:bg-dark-green-s.hover\:bg-green-3.dark\:hover\:bg-dark-green-3.h-\[28px\].select-none.rounded.px-5.text-\[13px\].leading-\[18px\]")
submit_button.click()

time.sleep(10)

# Clean up
driver.quit()