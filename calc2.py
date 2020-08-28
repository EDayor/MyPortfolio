#!/usr/bin/python3 

def addition(x, y):
    return x + y
    
def subtraction(x, y):
    return x - y 

def multiplication(x, y): 
    return x * y 

def division(x, y):
    return x / y
# These are the function we are using in the program    
# and the statement that will be returned for the result 

def main():
# This starts the program and says what 
# the functions that will be used will be 

    print("Basic Calculator 2")
    # String will be printed out on the string 
    
    var1 = int(input("What's your number:"))
    var2 = int(input("What's your number:"))
    # User will be prompted to input two different variables that must be integers 

    choice = input("Addition or subtraction or multiplication or division 
    ('add' or 'sub' or 'mul' or 'div')")
    # User will be asked to choose and input the type of calculation to do. 
   
    if choice == 'add':
        answer = addition(var1, var2)
        print("You chose addition: {var1} + {var2}")
        print(f"Your answer is {answer}")
    # String will be printed on the screen and the answer 
    # will be given from the variables inputted  
    # answer will be from the function (calculation user inputed)
        
    elif choice == 'sub':
        answer = subtraction(var1, var2)
        print("You chose subtraction: {var1} - {var2}")
        print(f"Your answer is {answer}")
    elif choice == 'mul':
        answer = multiplication(var1, var2)
        print("You chose multiplication: {var1} * {var2}")
        print(f"Your answer is {answer}")
    elif choice == 'div':
        answer = division(var1, var2)
        print(" You chose division: {var1} / {var2}")
        print(f"Your answer is {answer}")
     # Depending on the input given the string will be printed on the screen
     # along with answer to the equation from the variables given 
     # answer will be from the function (calculation user inputed)
     
    else:
        print("Please only type 'add' , 'sub' , 'mul' or 'div'")
    # This prompt will show on the screen if the user did not input 
    # the proper choices    
    
main()
# exiting the program 