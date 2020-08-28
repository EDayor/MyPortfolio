#!/usr/bin/python3 

# We are geting data from a module to use.
import getpass 
# This module allows the user to input a password 
# without showing it on the screen

loginDict = {"gjlamanno": "Speer2016" , "dTrump": "USA" , "Pythonboss": "CyberSecurity"}
# This is a dictionary of username and passwords (unique key-value pairs that must 
# match up when inputted)

count=0
while count <5:
    count += 1
# This begins the loop with the conditions that the user 
# only has five attempts.     
    
    username = input("Please enter your username: ") 
    password = getpass.getpass(prompt="Please enter your password: ")
    # User is prompted for a username and prompted for the password 
    # using the function from the getpass module imported 
    
    if username in loginDict and password == loginDict[username]:
        print("Logged in successfully as " + username)
        break 
    # This string is printed out if conditions are meet (username must in dictionary
    # and password must match the username it is paired with) and the loop ends 
     
    elif count == 5: 
        print("Out of Attempts! Goodby.")
        break
    # The user has used all attempts available and string
    # is printed out on the screen and the loop ends   
    
    else:
        print("Unsuccessful Login. Try Again.")
        continue 
    # After each failed attempt before the condition of five is meet the user 
    # sees this string printed out on the screen and the loop continues to 