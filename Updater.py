import time,requests,os,traceback,sys,json

with open("fortnite.py", encoding='utf-8') as f:
    current = f.read().replace('“','"').replace('”','"')
github = requests.get("https://raw.githubusercontent.com/LeakerByDragon3/LeakerByDragon3/main/fortnite.py").text.replace('“','"').replace('”','"')
if current != github:
    print('Update Gefunden! Bitte warten...')
    os.remove("fortnite.py")
    with open("fortnite.py", 'w') as f:
        f.write(github)
    print('Update Erfolgreich Heruntergeladen! Jetzt kannst du dein bot starten!')
elif current == github:
    print('Kein Update Gefunden!')
os.chdir(os.getcwd())
os.execv(os.sys.executable,['python','fortnite.py'])