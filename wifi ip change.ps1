function changeWifiIp {
    param(
        [string]$interfaceIndex,
        [string]$NewAddress,
        [string]$defaultGateWay
    )

    Get-NetIPConfiguration 

    $NewAddress = Read-Host "Enter the New IPAddress you want to assign (Make sure it is of same class) :- "
    $defaultGateWay = Read-Host "Enter the default gateway for wifi showing above :- "
    $interfaceIndex = Read-Host "Enter the InterfaceIndex for your wifi from information given above :- "

    $decision = $true
    do {
        ping $NewAddress
        if ($? -eq $false) {
            New-NetIPAddress -InterfaceIndex $interfaceIndex -IPAddress $NewAddress -PrefixLength 24 -DefaultGateway $defaultGateWay
            $decision = $false
        } else {
            Write-Host "The IP address $NewAddress is already in use. Please enter a different IP address."
            $NewAddress = Read-Host "Enter the New IPAddress you want to assign (Make sure it is of same class) :- "
        }
    } while ($decision -eq $true)

    Get-NetIPConfiguration
}

changeWifiIp
