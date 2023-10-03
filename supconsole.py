#!/usr/bin/env python3
# BackTrack

from os import system 
import sys
system("")

try:
    
    from colorama import Fore as f  
    import socket 
    import requests
    import time
    import builtwith
    import base64
    import EMN
    
except ModuleNotFoundError:
    system("pip install colorama && pip install requests && pip install builtwith && pip install EMN==0.0.0 && clear")



# Banner 

print(f"""{f.RED}
 ___ _   _ _ __  _ __ __ _
/ __| | | | '_ \| '__/ _` |
\__ \ |_| | |_) | | | (_| |
|___/\__,_| .__/|_|  \__,_|
          |_|
          
    {f.RED}+----------------------+
{f.RED}    |   {f.YELLOW}Supra {f.CYAN}FrameWork{f.RED}    |   
{f.RED}    +----------------------+
{f.RESET}
""")

# If argv is empty

if (args_count := len(sys.argv)) < 2:
    print(f"""{f.RED}[-]{f.YELLOW} USAGE: python supconsole.py <command>\n
{f.GREEN}[{f.YELLOW}!{f.GREEN}] {f.CYAN}HELP: {f.LIGHTBLACK_EX}python supconsole.py -h {f.RED}/{f.LIGHTBLACK_EX} python supconsole.py --help {f.RED}/{f.LIGHTBLACK_EX} python supconsole.py ?{f.RESET}""")
    
# Network Factory

elif sys.argv[1] == "-net" or sys.argv[1] == "--network":
        
    if (args_count := len(sys.argv)) < 3:
        print(f"""{f.RED}[-]{f.YELLOW} USAGE: python supconsole.py <command>\n
{f.GREEN}[{f.YELLOW}!{f.GREEN}] {f.CYAN}HELP: {f.LIGHTBLACK_EX}python supconsole.py -h {f.RED}/{f.LIGHTBLACK_EX} python supconsole.py --help {f.RED}/{f.LIGHTBLACK_EX} python supconsole.py ?{f.RESET}""")
    
    elif sys.argv[2] == "-ip":
        site = sys.argv[3]
        try:
            start = time.time()
            s = socket.gethostbyname(site)
            end = time.time()
            print(f"\n{f.BLUE}[{f.YELLOW}+{f.BLUE}]{f.RED} site {f.YELLOW}: {f.WHITE}{site}\n{f.BLUE}[{f.YELLOW}+{f.BLUE}]{f.RED} host {f.YELLOW}: {f.WHITE}{s}\n{f.BLUE}[{f.YELLOW}+{f.BLUE}]{f.RED} mission end in {f.YELLOW}: {f.WHITE}{end-start:.2f}\n")

        except:
            print(f"\n{f.RED}Faild ! Please Try Again")

    
    elif sys.argv[2] == "-html":
        site = sys.argv[3]
        try:
            start = time.time()
            html = requests.get(site).text
            end = time.time()
            print(f.WHITE,html+"\n\n"+f"{f.BLUE}[{f.YELLOW}+{f.BLUE}]{f.RED} mission end in {f.YELLOW}: {f.WHITE}{end-start:.2f}")

        except:
            print(f"{f.RED}[-]{f.RED} Faild ! Please Try Again")

    
    elif sys.argv[2] == "-s":
        site = sys.argv[3]
        try:
                start = time.time()
                req = requests.get(site).status_code
                end = time.time()
                print("\n"+f.WHITE+str(req)+f"{f.RED}\n{f.BLUE}[{f.YELLOW}+{f.BLUE}]{f.RED} mission end in {f.YELLOW}: {f.WHITE}{end-start:.2f}\n")

        except:
            print(f"{f.RED}[-] Faild ! Please Try Again")
    
    elif sys.argv[2] == "full-scan":
        site_Scan = sys.argv[3]
        try:
            start = time.time()
            _info = builtwith.builtwith(site_Scan)
            end = time.time()
            print(f.WHITE)
            print(_info)
            print(f"\n{f.BLUE}[{f.RED}+{f.BLUE}]{f.RED} mission end in {f.YELLOW}: {f.WHITE}{end-start:.2f}\n")
        except:
            print("")
            
    elif sys.argv[2] == "scan-port":
        _port = sys.argv[3]
        def open_port(host, port):
            s = socket.socket()
            try:
                s.connect((host, port))
                s.settimeout(0.2)
            except:
                return False
            
            else:
                return True
                
        for port in range(1,1023):
            if open_port(_port, port):
                print(f'{f.BLUE}[{f.RED}+{f.BLUE}] {f.YELLOW}{_port}{f.GREEN}:{f.YELLOW}{port} is open {f.RESET}')
            else:
                print(f'{f.BLUE}[{f.RED}-{f.BLUE}] {f.RED}{_port}{f.GREEN}:{f.RED}{port} is closed {f.RESET}')
    
    
    elif sys.argv[2] == "?" or sys.argv[2] == "-h" or sys.argv[2] == "--help":
        filea = open("net_con.txt", "r")
        print(f.WHITE+filea.read())
    
    
# Telegram Factory

elif sys.argv[1] == "-tel" or sys.argv[1] == "--telegram":
    if sys.argv[2] == "set-token":
        if sys.argv[4] == "set-chat-id":
            if sys.argv[6] == "set-msg":
                m = " ".join(sys.argv[7:])
                print(f"{f.BLUE}[{f.RED}+{f.BLUE}]{f.RED} Token = {f.YELLOW}{sys.argv[3]}")
                print(f"{f.BLUE}[{f.RED}+{f.BLUE}]{f.RED} Chat ID = {f.YELLOW}{sys.argv[5]}")        
                print(f"{f.BLUE}[{f.RED}+{f.BLUE}]{f.RED} Message = {f.YELLOW}{m}")
        
                print(f"\n{f.BLUE}[{f.MAGENTA}*{f.BLUE}] Wait For Send Message to Chat ID ...")
                try:
                    url = (f"https://api.telegram.org/bot{sys.argv[3]}/sendMessage?chat_id={sys.argv[5]}&text={m}")
                    payload = {
                        "UrlBox" : url,
                        "AgentList" : "Google Chrome",
                        "VersionList" : "HTTP/1.1",
                        "MethodList" : "GET"
                    }
                    start = time.time()
                    req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=payload).status_code
                    end = time.time()
                    
                    print(f"\n{f.BLUE}[{f.RED}+{f.BLUE}]{f.BLUE} Sended Successfuly !\n{f.BLUE}[{f.RED}+{f.BLUE}] Mission End in {f.RED}{end-start:.2f}")

                except:
                    print(f"{f.RED}[-] Cannot Send . Please Try Again")
                    
    elif sys.argv[2] == "?" or sys.argv[2] == "-h" or sys.argv[2] == "--help":
        fi = open("tel_con.txt", 'r')
        print(fi.read()) 
        
# Encrypt Factory

elif sys.argv[1] == "-enc" or sys.argv[1] == "--encrypt":
    if sys.argv[2] == "-b85":
        txt = " ".join(sys.argv[3:])
        print(EMN._encrypt(txt).b85())
    
    elif sys.argv[2] == "-b64":
        txt = " ".join(sys.argv[3:])
        print(EMN._encrypt(txt).b64())
    
    elif sys.argv[2] == "-b32":
        txt = " ".join(sys.argv[3:])
        print(EMN._encrypt(txt).b32())
    
    elif sys.argv[2] == "-b16":
        txt = " ".join(sys.argv[3:])
        print(EMN._encrypt(txt).b16())
        
    elif sys.argv[2] == "?" or sys.argv[2] == "-h" or sys.argv[2] == "--help":
        fia = open("enc_con.txt", 'r')
        print(fia.read())

elif sys.argv[1] == "-dec" or sys.argv[1] == "--decrypt":
    if sys.argv[2] == "-b85":
        txt = " ".join(sys.argv[3:])
        print(base64.b85decode(txt.encode("utf-8")))
    
    elif sys.argv[2] == "-b64":
        txt = " ".join(sys.argv[3:])
        print(base64.b64decode(txt.encode("utf-8")))
        
    elif sys.argv[2] == "-b32":
        txt = " ".join(sys.argv[3:])
        print(base64.b32decode(txt.encode("utf-8")))
    
    elif sys.argv[2] == "-b16":
        txt = " ".join(sys.argv[3:])
        print(base64.b16decode(txt.encode("utf-8")))
    
    elif sys.argv[2] == "-utf-8":
        txt = " ".join(sys.argv[3:])
        print(txt.encode("utf-8"))
    
    elif sys.argv[2] == "?" or sys.argv[2] == "-h" or sys.argv[2] == "--help":
        fas = open("dec_con.txt", 'r')
        print(fas.read())


elif sys.argv[1] == "?" or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    _help = open("help_file.txt", 'r')
    print(_help.read())
