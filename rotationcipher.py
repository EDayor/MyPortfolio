#!/usr/bin/python3

alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# This is the plaintext alphabet that will be 
# part of the table for the rotation cipher 

choice = input ("Will you 'encrypt' or 'decrypt' today?: ")
# Prompt will appear on screen asking the user to  
# choose and input the function they want to do. 

text = input("Enter your message: ")
# Prompt will appear on screen asking the user to input 
# what their message of choice for the function will be.  

rotation = int(input("Pick a number: "))
# Prompt will appear on screen asking the user to input 
# an integer that will be used in the function will be. 

def encrypt():
	result = ''
	for l in text: 
		index = ((alphabet.index(l) + rotation) % len(alphabet))
		i = alphabet[index]
		result += i
	print(result)
# The encrypt function has been defined for the message user inputed. The condition 
# is asking the function to find index of the letters in the text utilizing the integer 
# that was given. From that we are asking the function to use the alphabet range to 
# to figure out the index of the the new letter. This is done for each letter of 
# the message and the result is then printed. 

def decrypt():
	result = ''
	for l in text: 
		index = ((alphabet.index(l) - rotation) % len(alphabet))
		i = alphabet[index]
		result = result + i
	print(result)
# The decrypt function has been defined for the message user inputed. The condition 
# is asking the function to find index of the letters in the text utilizing the integer 
# that was given. From that we are asking the function to use the alphabet range to 
# to figure out the index of the the new letter. This is done for each letter of 
# the message and the result is then printed. 
	
if choice  == "encrypt": 
	encrypt()
# When the user chooses encrypt the encrypt function 
# will be used 
	
elif choice == "decrypt":
	decrypt()
# When the user chooses to decrypt the decrypt function 
# will be used. 
	
else:
	print("Input not recognized, please choose 'encrypt' or 'decrypt'")
	# This prompt will show up on the screen if the user did not input 
	# the proper choice. 