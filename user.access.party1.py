# IN: login , passw
# FACT:
# OUT:

# from database
SYS_LOGIN  = "admin"  #str
SYS_PASSW  = "1234"   #str

# from user input
login     = input("login:")
passw     = input("pass:")

#login
hasAcceess = SYS_LOGIN == login and SYS_PASSW== passw

if hasAcceess:
    print("Acees grander !")
else:
    print("Acces DENIED !") 
    


