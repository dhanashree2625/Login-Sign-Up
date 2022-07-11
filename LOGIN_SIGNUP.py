import json
import re

print("*********WELCOME TO LOGIN/SIGNUP PAGE***********")
# Account=input("Enter The login or signup :")
user=input("Do you want to \n1.)signup\n2.)login:")
if user=="signup":
    username=input("Enter your username :")
    print("Create a strong password Use specail characters.")
    password1=input("Enter ur password :")
    if re.search("[a-z A-Z]",password1) and re.search("[@%$#!]",password1) and re.search("[0-9]",password1) :
        password2=input("Enter your password again :")
        if password1==password2 :
            print("Confirm password:")
            date_of_birth=input("enter your date of birth :")
            contact=int(input("Enter Your mobile number :"))
            email=input("enter the email")
            dic=({"username":username,"password":password1,"re_password":password2,"date_of_birth":date_of_birth
            ,"contact":contact,"email":email})
            file=open("data signup.json","a")
            json.dump(dic,file,indent=4)
        else :
            print("password not matching")
    else :
        print("weak password please use special charcters")
else:
    if user=="login" :
        username=input("enter your username :") 
        password=input("enter the password :")
        with open("data signup.json","r") as file1 :
            a=file1.read() 
            b=json.loads(a)
            if b["username"]==username :
                if b["password"]==password :
                    print("login successful")
                else :
                    print("wrong password")
            else :
                print("wrong username")
    else :
        print("wrong id")                        


    
    
    


	
