password = "Marvin"
from getpass import getpass

guess_count = 0

guess_limit = 3

while guess_count < guess_limit :
    guess = input("input password : ")
    
    print(" password entered : " + "*" * len(guess))
    
    guess_count +=1 
    if guess == password :
        print(" WELCOME ") 
        break
    elif guess != password :
        print("Try again")
else :
    print("Access Denied")
    
        

    
    
    
