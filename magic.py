#!/user/bin/python3

# We are geting data from a module to use.
import sys
# This module has functions that give instructions to how the 
# script will work with the host system. 
import random
# This module has a different things to do with the random number generation. 

ans = True
# When the conditions are meet the statements will be printed. 

while ans:
# This loop executes statements (an answer) if certain conditions 
# are meet (user inputting a question) 
    question = input("Ask the magic 8 ball a question: (press enter to quit)")
# This is the message that will display on the output screen asking 
# the user to input a question or you can quit. 
 
    answers = random.randint(1,8)
# This will generate a random answer to the question the user inputed within the range given.    

    if question == "":
        sys.exit()
# If the user inputs a question the program will genrate a 
# random answer in the form of a string.
# There is a function allowing you to exit the the program. 
 
    elif answers == 1:
        print ("It is certain")
    
    elif answers == 2:
        print ("Outlook good")
    
    elif answers == 3:
        print ("You may rely on it")
    
    elif answers == 4:
        print ("Ask again later")
    
    elif answers == 5:
        print ("Concentrate and ask again")
    
    elif answers == 6:
        print ("Reply hazy, try again")
    
    elif answers == 7:
        print ("My reply is no")
    
    elif answers == 8:
        print ("My sources say no")
# When the user inputs a question that meets the conditions a random answer string 
# will be printed that corresponds to the number. 