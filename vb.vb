Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\Projects\Python\PrimeProgressTweeter\create_task.bat" & Chr(34), 0
Set WshShell = Nothing