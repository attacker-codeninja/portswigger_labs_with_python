# Hack Steps

1. Fetch 1.txt log file
2. Extract carlos password from the log file
3. Login as carlos

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python insecure_direct_object_references.py
```

# Expected Output

```
1. Fetching 1.txt log file.. OK
2. Extracting password from the log file.. OK => daxpy2ozi7znnixdcgkh
3. Fetching login page to get valid session and csrf token.. OK
4. Logging in as carlos.. OK
5. Fetching carlos profile.. OK
🗹 Check your browser, it should be marked now as solved
```
