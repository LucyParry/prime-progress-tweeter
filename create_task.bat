@echo off
:: Command for setting up the task scheduler task
schtasks /create /tn PrimeProgressTweeter /tr C:\Projects\Python\PrimeProgressTweeter\run_tweet.bat /sc HOURLY