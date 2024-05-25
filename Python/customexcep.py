class Invalidpinerror(Exception):
    pass
    
def check():
    pin=int(input("Enter pin: "))
    originalpin=1234;
    c=0;
    if(pin==originalpin):
        print("logged in sucessfull")
    else:
        raise Invalidpinerror
    
try:
    check()
except:
    print("invalid pin,two attempts left")
    try:
        check()
    except:
        print("invalid pin,one attempts left")
        try:
           check()
        except:
           print("Locked.....!") 
        
