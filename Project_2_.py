# Password strenght check
import re

def Password_Checker(Password):
    
    if len(Password)<6:
        return "Weak : Pasword must be at least 6 character"
    if not any(char.isdigit() for char in Password):
        return "Weak : Pasword must contain numbers"
    if not any(char.isupper() for char in Password):
        return "Weak : Pasword must contain upper letters"
    if not any(char.islower() for char in Password):
        return "Weak : Pasword must contain lower letters"
    if not re.search(r"[!@#$%^&*()*]",Password):
        return "Medium : Pasword must contain special letters"
    
    return "Strong : Password is strong"    
    
def Password_Take():
    print("Welcome , in password checher")
    while True:
        check=input("Do you want to check your password (y/n) ")
        if check.lower()=="y".lower():
            user=input("Plzz Enter your passsword ")
            result=Password_Checker(user)
            print(result)
            if result=="Strong : Password is strong":
                break
            
        elif check.lower()=="n".lower():
             print("Thany You")
             break           
        
        else:
            print("Ivalid Output")
                 
    
    
Password_Take()
    