function Set-Permission
{
param([string[]]$FilePath,
[string[]]$UserName,
[string[]]$GivePermission)

   $FilePath = Read-Host "Enter path of the file :- "
   $UserName = Read-Host "Enter the User-Name to whom permission is being granted :- "
   $GivePermission = Read-Host "Enter the permission that you want to grant :- "

   $Acl = Get-Acl -Path "$FilePath"
   $AccessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("$UserName" , "$GivePermission" , "Allow")
   $Acl.SetAccessRule($AccessRule)
   $Acl | Set-Acl -Path "$FilePath"
   (Get-Acl -Path "$FilePath").Access | Format-Table 
}


Set-Permission
