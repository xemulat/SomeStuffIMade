from os import system
from urllib.request import urlretrieve
from sys import exit
from time import sleep

# Completely unoptimized shitty code starts here:
        
def cls():  # better (but still shitty) cls function
    system('cls')

def powpow(name, rep_name, rep_link):   # Downloader
    print(f"Downloading {name}...")
    urlretrieve(rep_link, rep_name, reporter)
    print(f'{name} Downloaded!')
    
print("Welcome, This small Python script will download Programs for you!\n"
      "Now choose your programs:\n"
      "(Y/n)\n")
internettools = input("Download Internet Tools: ")
gaming = input("Download Gaming Software: ")
basicredists = input("Download Redists: ")
tools = input("Download Tools: ")
office = input("Download Office (cracked): ")
crackingandpatches = input("Download Cracking Software: ")
wintweaker = input("Download WinaeroTweaker: ")
drivers = input("Download Drivers: ")
programming = input("Download Programming stuff: ")
personalization = input("Download Personalization tools: ")
keepass = input("Download KeePassXC: ")
    
powpow('7-Zip', '7zip.exe', 'https://www.7-zip.org/a/7z2200-x64.exe')
if internettools == 'y':
    powpow('Internet Tools', 'Internet.zip', 'https://github.com/xemulat/MyFilesForDDL/releases/download/pctools/InternetTools.zip')

if gaming == 'y':
    powpow('Gaming Software', 'Gaming.zip', 'https://github.com/xemulat/MyFilesForDDL/releases/download/pctools/Gaming.zip')

if basicredists == 'y':
    powpow('BasicRedists', 'BasicRedists.zip', 'https://github.com/xemulat/MyFilesForDDL/releases/download/pctools/BasicRedists.zip')

if tools == 'y':
    powpow('Tools', 'tools.zip', 'https://github.com/xemulat/MyFilesForDDL/releases/download/pctools/tools.zip')

if office == 'y':
    powpow('Office + Activator', 'Office.exe', 'https://github.com/xemulat/MyFilesForDDL/releases/download/pctools/OfficeSetup.exe')

if crackingandpatches == 'y':
    powpow('Cracking And Patching Stuff', 'CrackPatch.zip', 'https://github.com/xemulat/MyFilesForDDL/releases/download/pctools/cracking.zip')

if wintweaker == 'y':
    powpow('Winaero Tweaker', 'WinaeroTweaker.zip', 'https://winaerotweaker.com/download/winaerotweaker.zip')

if drivers == 'y':
    powpow('Drivers', 'Drivers.zip', 'https://github.com/xemulat/MyFilesForDDL/releases/download/pctools/drivers.zip')

if programming == 'y':
    powpow('VSCoduim', 'VSCodium.msi', 'https://github.com/VSCodium/vscodium/releases/download/1.68.1/VSCodium-x64-1.68.1.msi')

if keepass == 'y':
    powpow('KeePassXC', 'KeePass.msi', 'https://github.com/keepassxreboot/keepassxc/releases/download/2.7.1/KeePassXC-2.7.1-Win64.msi')
        
if personalization == 'y':
    powpow('Personalization Utils', 'Personalization.zip', 'https://github.com/xemulat/MyFilesForDDL/releases/download/pctools/personalization.zip')
        
        
print("\n"
      "All done!")
exit(sleep(6))
    