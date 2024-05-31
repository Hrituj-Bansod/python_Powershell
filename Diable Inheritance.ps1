function DisableInheritance
{param([string[]]$FilePath)

$FilePath = Read-Host "Enter the path of the folder on which you want to Disable the Inheritance :- "

$Acl = Get-Acl -Path $FilePath
$Acl.SetAccessRuleProtection($true,$true)
$Acl | Set-Acl $FilePath
(Get-Acl D:\newFolerDemoWala\owner2).Access | Format-Table *
}

DisableInheritance