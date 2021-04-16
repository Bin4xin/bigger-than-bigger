strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colItems = objWMIService.ExecQuery("Select deviceid,loadpercentage from Win32_Processor ",,48)
Wscript.Echo "deviceid"&vbTab&"loadpercentage"
For Each objItem in colItems
Wscript.Echo objItem.deviceid&vbTab&objItem.LoadPercentage
Next