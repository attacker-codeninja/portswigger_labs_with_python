# Hack Steps

1. Fetch the feedback page
2. Extract csrf token and session cookie
3. Inject payload into the name field when submitting a feedback to execute the `whoami` command and exfiltrate the output via a DNS query to burp collaborator.
4. Check your burp collaborator for the output of the `whoami` command


# Run Script

1. Change the URL of the lab
2. Change the domain of the burp collaborator
3. Start script

```
~$ python blind_os_command_injection_with_out_of_band_data_exfiltration.py
```

# Expected Output

```
⟪#⟫ Injection parameter: name
⦗1⦘ Fetching the feedback page.. OK
⦗2⦘ Extracting csrf token and session cookie.. OK
⦗3⦘ Injecting payload to execute the `whoami` command and exfiltrate the output via a DNS query to burp collaborator.. OK
🗹 Check your burp collaborator for the output of the `whoami` command then submit the answer
```
