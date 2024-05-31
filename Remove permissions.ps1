function Remove-Permission
{
param([string[]]$FilePath,
[string[]]$UserName,
[string[]]$GivePermission)

   $FilePath = Read-Host "Enter path of the file :- "
   $UserName = Read-Host "Enter the User-Name who's permission are being removed :- "
   $GivePermission = Read-Host "Enter the permission that you want to Remove :- "

   $Acl = Get-Acl -Path "$FilePath"
   $AccessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("$UserName" , "$GivePermission" , "Allow")
   $Acl.RemoveAccessRule($AccessRule)
   $Acl | Set-Acl -Path "$FilePath"

   (Get-Acl -Path "$FilePath").Access | Format-Table 
}


Remove-Permission
