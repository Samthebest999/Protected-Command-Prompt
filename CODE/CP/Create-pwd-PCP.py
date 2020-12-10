import time, os
#Create Password for PROTECTED COMMAND PROMPT!!!
print("Hello It's time to create a password for your Protected Command Prompt!!!")
print("""
INSTRUCTIONS
++++++++++++
============
++++++++++++
1. Move this file to the directory in which you have installed your Protected Command Prompt.py
2. Relax!! as Python will Ask you for your chosen password and then You are done!!!
""")
fp = input("What is your chosen password???")
sp = input("Confirm Password")
if fp == sp:
    break
else:
    print("Passwords Don't Match :(")
    print("Now the program will close in 5 seconds!!")
    time.sleep(6)
    quit()
cenv = open("p.env","w")
cenv.write(fp)
print("DONE!!")
print("BTW if you need to reset your password you can use this program!!")
os.system("del /f pcfc.py")
os.system("rm pcfc.py")
