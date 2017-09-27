@echo off
schtasks /create /tn PrimeProgressTweeter /tr C:\Projects\Python\PrimeProgressTweeter\run_tweet.bat /sc HOURLY