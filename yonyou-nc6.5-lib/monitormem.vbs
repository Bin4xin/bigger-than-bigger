strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")

Set colItems = objWMIService.ExecQuery("Select * from Win32_PhysicalMemory",,48)
For Each objItem in colItems
memory = CDbl(memory) + CDbl(objItem.capacity)
Next
set objRefresher = CreateObject("WbemScripting.SWbemRefresher")
Set objMemory = objRefresher.AddEnum _
(objWMIService, "Win32_PerfFormattedData_PerfOS_Memory").objectSet
objRefresher.Refresh
objRefresher.Refresh
objRefresher.Refresh
For each myMemory in objMemory
Wscript.Echo "total"&vbtab&"free"&vbtab&"used"
Wscript.Echo  memory/1024/1000 &vbtab&myMemory.AvailableBytes/1024/1000&vbtab&myMemory.CommittedBytes/1024
Next