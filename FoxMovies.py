name = input("Movie Name: ")
subtitles = input("Subtitles Type: ")
quality = input("Quality: ")
denoise = input("De-Noise: ")
gofile1 = input("Gofile 1 Link: ")
gofile2 = input("Gofile 2 Link: ")
anon1 = input("Anon 1 Link: ")
anon2 = input("Anon 2 Link: ")
bay1 = input("Bay 1 Link: ")
bay2 = input("Bay 2 Link: ")
print("")
print("Site:")

if gofile1 == '':
    gofile1l = ''
else:
    gofile1l = '[GoFile 1](' + gofile1 + '), '

if gofile2 == '':
    gofile2l = ''
else:
    gofile2l = '[GoFile 2](' + gofile2 + '), '
    
if bay1 == '':
    bay1l = ''
else:
    bay1l = '[BayFiles 1](' + bay1 + '), '
    
if bay2 == '':
    bay2l = ''
else:
    bay2l = '[BayFiles 2](' + bay2 + '), '
    
if anon1 == '':
    anon1l = ''
else:
    anon1l = '[AnonFiles 1](' + anon1 + '), '
    
if anon2 == '':
    anon2l = ''
else:
    anon2l = '[AnonFiles 2](' + anon2 + ')'
    
first_char = name[0]

print("Site:")
print("- " + name + " - " + gofile1l + gofile2l + anon1l + anon2l + bay1l + bay2l)
print(" ")
print("Discord:")
print("Name: " + name)
print("Enconded by NightlyFox")
print("Subtitles: " + subtitles)
print("Quality: " + quality)
print("De-Noise: " + denoise)
print("Link: https://rentry.co/NightlyFoxMovies#" + first_char)
input(" ")
input(" ")