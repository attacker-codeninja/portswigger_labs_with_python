## Hack Steps

1. Fetch the login page
2. Extract the csrf token and session cookie to login
3. Login as content-manager
4. Fetch a product template
5. Extract the csrf token to edit the template
6. Edit the template and inject the malicious payload
7. Fetch the product page after editing to execute the payload
8. Extract the secret key
9. Submit the solution

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting the csrf token and session cookie to login.. OK
⦗3⦘ Logging in as content-manager.. OK
⦗4⦘ Fetching a product template.. OK
⦗5⦘ Extracting the csrf token to edit the template.. OK
⦗6⦘ Editing the template and injecting the malicious payload.. OK
⦗7⦘ Fetching the product page after editing to execute the payload.. OK
⦗8⦘ Extracting the secret key.. OK => w640pgeh48x5mdnp9gxazgz0nlecfmpp
⦗9⦘ Submitting the solution.. OK
🗹 The lab should be marked now as solved
```
