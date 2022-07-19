gamename = input("Game name: ")
crack = input("Crack: ")
version = input("Version: ")
uncompressed = input("Game size UnCompressed: ")
compressed = input("Game size Compressed: ")
lore = input("Game info: ")
print("Download Links")
gdrive = input("GDrive link: ")
gofile1 = input("GoFile 1 link: ")
gofile2 = input("GoFile 2 link: ")
gofile3 = input("GoFile 3 link: ")
anon1 = input("AnonFiles 1 link: ")
anon2 = input("AnonFiles 2 link: ")
anon3 = input("AnonFiles 3 link: ")
onedrive = input("OneDrive link: ")
bayfiles = input("BayFiles link: ")
magnet = input("Magnet link: ")

print("Generating...")
print("cs.rin.ru:")
print("")
print("Repacker - NightlyFox")
print("Game - " + gamename)
print("Crack - " + crack)
print("Version - " + version)
print("Size Uncompressed - " + uncompressed)
print("Size Compressed - " + compressed)
print("Game Info - " + lore)
print("")
print("Download Links:")
if gdrive == '':
    print("GDrive - File too big sorry")
else:
    print("GDrive - [url]" + gdrive + "[/url]")

if gofile1 == '':
    print("GoFile 1 - File too big sorry")
else:
    print("GoFile 1 -[url] " + gofile1 + "[/url]")

if gofile2 == '':
    print("GoFile 2 - File too big sorry")
else:
    print("GoFile 2 -[url] " + gofile2 + "[/url]")

if gofile3 == '':
    print("GoFile 3 - File too big sorry")
else:
    print("GoFile 3 - [url]" + gofile3 + "[/url]")

if anon1 == '':
    print("AnonFiles 1 - File too big sorry")
else:
    print("AnonFiles 1 - [url]" + anon1 + "[/url]")

if anon2 == '':
    print("AnonFiles 2 - File too big sorry")
else:
    print("AnonFiles 2 - [url]" + anon2 + "[/url]")

if anon3 == '':
    print("AnonFiles 3 - File too big sorry")
else:
    print("AnonFiles 3 - [url]" + anon3 + "[/url]")

if onedrive == '':
    print("OneDrive - File too big sorry")
else:
    print("OneDrive - [url]" + onedrive + "[/url]")

if bayfiles == '':
    print("BayFiles - File too big sorry")
else:
    print("BayFiles - [url]" + bayfiles + "[/url]")
    
if magnet == '':
    print("Magnet - File too big sorry")
else:
    print("Magnet - [url]" + magnet + "[/url]")
    


print("")
print("Site: [url]https://rentry.co/NightlyFoxRepacks[/url]")

print("")
print("Site:")
if gdrive == '':
    gdrivel = ''
else:
    gdrivel = '[GDrive](' + gdrive + '), '

if gofile1 == '':
    gofile1l = ''
else:
    gofile1l = '[GoFile 1](' + gofile1 + '), '

if gofile2 == '':
    gofile2l = ''
else:
    gofile2l = '[GoFile 2](' + gofile3 + '), '

if gofile3 == '':
    gofile3l = ''
else:
    gofile3l = '[GoFile 3](' + gofile3 + '), '

if anon1 == '':
    anon1l = ''
else:
    anon1l = '[AnonFiles 1](' + anon1 + '), '

if anon2 == '':
    anon2l = ''
else:
    anon2l = '[AnonFiles 2](' + anon2 + '), '

if anon3 == '':
    anon3l = ''
else:
    anon3l = '[AnonFiles 3](' + anon3 + '), '

if onedrive == '':
    onedrivel = ''
else:
    onedrivel = '[OneDrive](' + onedrive + '), '

if bayfiles == '':
    bayl = ''
else:
    bayl = '[BayFiles](' + bayfiles + '), '
    
if magnet == '':
    magl = ''
else:
    magl = '[Magnet](' + magnet + ')'
    

gamenan = gamename + ".txt"
print("- " + gamename + " - " + gdrivel + gofile1l + gofile2l + gofile3l + anon1l + anon2l + anon3l + onedrivel + bayl + magl)

line1 = "GDrive - " + gdrive + "   "
line2 = "GoFile 1 - " + gofile1 + "   "
line3 = "GoFile 2 - " + gofile2 + "   "
line4 = "GoFile 3 - " + gofile3 + "   "
line5 = "AnonFiles 1 - " + anon1 + "   "
line6 = "AnonFiles 2 - " + anon2 + "   "
line7 = "AnonFiles 3 - " + anon3 + "   "
line8 = "OneDrive - " + onedrive + "   "
line9 = "BayFiles - " + bayfiles + "   "
line10 = "Magnet - " + magnet + "   "

with open(gamenan, 'w') as f:
    f.writelines([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10])
    f.close()
    
input(" ")
input(" ")