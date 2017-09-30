' (Called from .py file) - Runs the given batch file and returns stdout

Dim batchFilePath
Dim returnString

If WScript.Arguments.Count = 0 Then
    WScript.Echo "Error - Missing batch script name parameter"
Else
    batchFilePath = WScript.Arguments(0)
    Set WshShell = CreateObject("WScript.Shell")

    On Error Resume Next
    Set WshShellExec = WshShell.Exec(batchFilePath)

    If Err.Number <> 0 Then
        WScript.Echo "Error - Could not run batch script " & batchFilePath & " - Has it been moved, renamed or deleted?"         
    Else
        returnString = WshShellExec.StdOut.ReadAll
        Wscript.echo returnString
    End If
    Err.Clear

    Set WshShell = Nothing
    Set WshShellExec = Nothing
End If