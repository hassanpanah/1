import subprocess

# Define the PowerShell command
command = '$swapButtons = Add-Type -MemberDefinition @'
[DllImport("user32.dll")]
public static extern bool SwapMouseButton(bool swap);
'@ -Name "NativeMethods" -Namespace "PInvoke" -PassThru
 
# Use $true for left-handed mouse and $false for right-handed mouse.
[bool]$returnValue = $swapButtons::SwapMouseButton($false)'

# Execute the PowerShell command
result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)

# Print the output
print(result.stdout)
