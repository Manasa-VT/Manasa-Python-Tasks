#! USR/BIN/PYTHon

#While loop in python

def user_info():
    while True:
        name=str(input("Enter your name:"))
        if len(name)>=6:
           print("Uset is valid we know",name)
           break
       
        else:
           print ("Invalid user, username must be 6 or more characters along with alphanumeric and UPPERCASRE")
def password_info():
     while True:
         password=str(input("Enter your password:"))
         if len(password) < 8:
            print("Invalid password, password must contan 8 or above  chars")
         else:
           print("Validate password, welcome to system login!")
           break

user_info()
password_info()


