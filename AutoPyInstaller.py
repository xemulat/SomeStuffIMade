from os import system
from colorama import init, Fore
init(autoreset=True)

system("cls")

def lprint(text: str):
    print(Fore.RED, '[S>] ' + text)

file = input("File: ")
uac = input("Use UAC: ")

file = '"' + file + '"'

if uac == 'y':
    uacl = " --uac-admin"
else:
    uacl = ""

system('pyinstaller --noconfirm --onefile --console --upx-dir "C:/Users/xemulated/Desktop/upx-3.96-win64" --clean ' + uacl + '  ' + file)
system("explorer dist")
system("rmdir build")
system("rm *.spec")