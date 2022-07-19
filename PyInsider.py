from lastversion import latest
from os import startfile
from colorama import init, Fore
from urllib.request import urlretrieve
import zipfile
init(autoreset=True)

print("PLEASE RUN AS ADMIN")
input(": ")

def lprint(text: str):
    print(Fore.RED, '[S>] ' + text)

lprint("Downloading latest version...")
lastver = latest(repo='abbodi1406/offlineinsiderenroll', output_format='version')
urlretrieve('https://github.com/abbodi1406/offlineinsiderenroll/releases/download/' + str(lastver) + '/OfflineInsiderEnroll-' + str(lastver) + '.zip', 'OfflineInsiderEnroll-' + str(lastver) + '.zip')
with zipfile.ZipFile('OfflineInsiderEnroll-' + str(lastver) + '.zip', 'r') as zip_ref:
    zip_ref.extractall()
startfile('OfflineInsiderEnroll.cmd')