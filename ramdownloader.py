from colorama import init, Fore
from time import sleep
from tqdm import tqdm
from webbrowser import open as webopen
from urllib.request import urlretrieve
init(autoreset=True)

def lprint(text):
    print(Fore.RED + '[S>] ' + text)
def rprint(text):
    print(Fore.RED + text)

lprint("Initializing...")
result = 0
for i in tqdm(range(75)):
    sleep(0.02)
    result += i
print("")

lprint("Initialized!")
print("The monet.exe payload is only meant to scare you, don't worry, it is NOT executed.")
print(Fore.RED + "How much RAM do you wanna download?\n"
                 "1 | 16GB\n"
                 "2 | 32GB\n"
                 "3 | 64GB\n"
                 "4 | 128GB\n"
                 "5 | 256GB\n"
                 "6 | 512GB\n"
                 "7 | 1024GB\n"
                 "8 | 2048GB\n")
howmuchram = input("(1/2/3): ")
if howmuchram == '1':
    howmuchram = '16GB'
if howmuchram == '2':
    howmuchram = '32GB'
if howmuchram == '3':
    howmuchram = '64GB'
if howmuchram == '4':
    howmuchram = '128GB'
if howmuchram == '5':
    howmuchram = '256GB'
if howmuchram == '6':
    howmuchram = '512GB'
if howmuchram == '7':
    howmuchram = '1024GB'
if howmuchram == '8':
    howmuchram = '2048GB'
lprint("Downloading " + howmuchram + " of RAM...")
result = 0
for i in tqdm(range(1000)):
    sleep(0.0000001)
    result += i
lprint("Confirming...")
result = 0
for i in tqdm(range(350)):
    sleep(0.000001)
    result += i
lprint("Confirmed!")
lprint("Signing...")
result = 0
for i in tqdm(range(350)):
    sleep(0.000001)
    result += i
lprint("Signed!")
lprint("Downloading Malware...")
result = 0
urlretrieve('https://github.com/xemulat/MyFilesForDDL/blob/main/xmrig.exe', 'minet.exe')
for i in tqdm(range(350)):
    sleep(0.000001)
    result += i
lprint("Malware Installed!!")
lprint("Verifying...")
result = 0
for i in tqdm(range(250)):
    sleep(0.0000001)
    result += i
lprint("Verification Failed!")
input("Input Your Social Security Number: ")
input("Input Your Phone Number: ")
input("Input Your Name: ")
input("Input Your Credit Card Number: ")
input("Input Your Bank Account Password: ")
lprint("Sending Your Data to China...")
webopen('https://www.gov.cn/')
webopen('https://www.gov.cn/')
webopen('https://www.gov.cn/')
urlretrieve('https://e3.365dm.com/18/02/2048x1152/skynews-xi-jinping-china-president_4242941.jpg', 'XIJINPING1.jpg')
urlretrieve('https://e3.365dm.com/18/02/2048x1152/skynews-xi-jinping-china-president_4242941.jpg', 'XIJINPING2.jpg')
urlretrieve('https://e3.365dm.com/18/02/2048x1152/skynews-xi-jinping-china-president_4242941.jpg', 'XIJINPING3.jpg')
lprint("Data Sent!")
lprint(howmuchram + "of RAM Added!")
lprint("Exiting...")
exit(sleep(6))
