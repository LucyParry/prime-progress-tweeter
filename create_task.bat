@echo off
:: Command for setting up the task scheduler task
schtasks /create /tn PrimeProgressTweeterTask /tr C:\Projects\Python\PrimeProgressTweeter\run_tweet.bat /sc HOURLY /mo 3