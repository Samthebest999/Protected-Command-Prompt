#Protected Command Prompt!!
import os
os.system("pip install requests")
import requests
cp = input("Would You like to create or reset your password? (Y/N case sensitive)")
if cp == "Y":
    durl= "https://raw.githubusercontent.com/Samthebest999/Protected-Command-Prompt/main/CODE/CP/Create-pwd-PCP.py"
    a = requests.get(durl, allow_redirects=True)
    open("Create-pwd-PCP.py", "wb").write(a.content)
    os.system("python Create-pwd-PCP.py")

ap = open("p.env","r")
uep = input("Password:")
if ap == uep:
    print("Cool You've Entered the Right Password!!")
    name = input("Please Enter Your Username")
    time.sleep(2)
    num = 0
    while num == 0:
        cmd = input("$" + name + ":")
else:
    print("Wrong Password")
    print("BYE")
    time.sleep(3)
    quit()
