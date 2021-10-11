import re
v=input("Enter the password:")
def funcheck(v):
    if(len(v)>=8):
        if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
            print(True)
        else:
            print(False)                              
    else:
        print(False)
funcheck(v)
