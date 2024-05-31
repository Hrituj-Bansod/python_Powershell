Write-Output "Process Management"

$num = Read-Host "Select the option.
1. Show all the processes.
2. Search process by it's name.
3. Search process by it's ID.
4. Show 10 processes consuming amount most of CPU.
5. Show 10 processes having most no. of handles.
6. Show 10 processes consuming least amount of CPU.
7. Show 10 processes having least no. of handles.`n"


switch($num){
1 {
Get-Process
}

2 {
$name = Read-Host "Enter the name of the process "
Get-Process -Name $name
}

3 {
$id = Read-Host "Enter the ID of the process "
Get-Process -Id $id
}

4 {
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
}

5 {
Get-Process | Sort-Object Handles -Descending | Select-Object -First 10
}

6 {
Get-Process | Sort-Object CPU -Descending | Select-Object -Last 10
}

7 {
Get-Process | Sort-Object Handles -Descending | Select-Object -Last 10
}

default { Write-Output "Invalid Option !"}
}