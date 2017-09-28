@echo off
:: Gets the verbose tasklist for the prime95.exe and outputs as a list
tasklist /v /fi "IMAGENAME eq prime95.exe" /fo LIST