## Hack Steps

1. Inject payload in 'category' query parameter to retrieve the name of users table
2. Adjust the payload to retrieve the names of username and password columns
3. Adjust the payload to retrieve the administrator password
4. Fetch the login page
5. Extract the csrf token and session cookie
6. Login as the administrator
7. Fetch the administrator profile

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗#⦘ Injection parameter: category
⦗1⦘ Injecting a payload to retrieve the name of users table.. OK => USERS_CTDTXL
⦗2⦘ Adjusting the payload to retrieve the names of username and password columns.. OK => USERNAME_ZOKPMB | PASSWORD_IZEVGS
⦗3⦘ Adjusting the payload to retrieve the administrator password.. OK => wurk7ay3uhjzxc8owsg9
⦗4⦘ Fetching the login page.. OK
⦗5⦘ Extracting the csrf token and session cookie.. OK
⦗6⦘ Logging in as the administrator.. OK
⦗7⦘ Fetching the administrator profile.. OK
🗹 The lab should be marked now as solved
```
