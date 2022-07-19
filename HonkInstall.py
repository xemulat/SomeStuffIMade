from urllib.request import urlretrieve
import sys
from time import sleep
from webbrowser import open as webopen
from os import system, startfile, remove as rm
from socket import gethostbyname, create_connection
from colorama import Fore, init
init(autoreset=True)

# Progress Bar And Size Reporter
def reporter(block_num, block_size, total_size):
    read_so_far = block_num * block_size
    if total_size > 0:
        percent = read_so_far * 1e2 / total_size
        print(f"\r{percent:5.1f}% {read_so_far:{len(str(total_size))}} out of {total_size}", end='')
        if read_so_far >= total_size:
            print()
    else:
        print(f"read {read_so_far}", end='')


# UrlRetriever
def powpow(name, rep_name, rep_link):
    print(f"Downloading {name}...")
    urlretrieve(rep_link, rep_name, reporter)
    print(f'{name} Downloaded!')
    startfile(rep_name)


# Check Is Internet Connection
def is_connected():
    try:
        return create_connection((gethostbyname('github.com'), 80), 2)
    except gaierror:
        return False

#TESTING! Optimized print function
def BPrint(prent):
    print(Fore.BLUE + prent)

def RPrint(prentr):
    print(Fore.RED + prentr)

def WPrint(prentw):
    print(Fore.WHITE + prentw)

#Main
system('cls')
RPrint("[S>] Testing Internet...")
system('cls')
RPrint("[S>] Internet is connected")
print(" ")
WPrint("Welcome, This small Python script will install selected GooseMod version for you!")
WPrint("All credits to GooseNest Team")
RPrint("THIS SCRIPT MUST BE RUN AS ADMINISTRATOR!!!")
BPrint("1. OpenAsar For Discord Stable")
BPrint("2. OpenAsar For Discord PTB")
BPrint("3. OpenAsar For Discord Canary")
BPrint("4. GooseMod For Discord Stable")
BPrint("5. GooseMod For Discord Public Test Build (PTB)")
BPrint("6. GooseMod For Discord Canary")
BPrint("7. GooseMod For Discord Developer (NOT Canary)")
BPrint("8. GooseMod For Discord Web")
BPrint("99. Exit")
gosever = input("(1/2/3/4/5/6/7/8/99): ")
print(" ")

if gosever == '1':
    powpow('OpenAsar Discord Stable', 'OADS.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/openasar/openasarstable.bat')

if gosever == '2':
    powpow('OpenAsar Discord Stable', 'OADP.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/openasar/openasarptb.bat')

if gosever == '3':
    powpow('OpenAsar Discord Canary', 'OADC.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/openasar/openasarcanary.bat')

if gosever == '4':
    powpow('GooseMod Discord Stable', 'GMDS.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/goosemod/goosemodstable.bat')

if gosever == '5':
    powpow('GooseMod Discord PTB', 'GMDP.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/goosemod/goosemodptb.bat')

if gosever == '6':
    powpow('GooseMod Discord Canary', 'GMDC.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/goosemod/goosemodcanary.bat')

if gosever == '7':
    powpow('GooseMod Discord Development', 'GMDD.bat', 'https://github.com/xemulat/MyFilesForDDL/releases/download/goosemod/goosemoddev.bat')

if gosever == '8':
    webopen('https://chrome.google.com/webstore/detail/goosemod-for-web/clgkdcccmbjmjdbdgcigpocfkkjeaeld')
    print("GooseMod For Discord Web URL Opened!")
    exit(sleep(3))
    
if gosever == '99':
    exit(sleep(2))