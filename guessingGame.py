# Guessing game, where the user has to guess a number between 1 and 100. The program will give hints if the guess is too high or too low. And also the program will keep track of the number of attempts made by the user. The game will continue until the user guesses the correct number or chooses to exit the game.

import random
computerSelectedRandomNumber = random.randint(1, 101)

userInput = int(input("Guess the number: "))

if userInput == computerSelectedRandomNumber:
		print("Wow!!! You guessed the correct number in 1st attempt.")

count = 1
while userInput != computerSelectedRandomNumber:
	count +=1
	if userInput > computerSelectedRandomNumber:
		print("Guess lower number")
		userInput = int(input("Guess the number again: "))

	elif userInput < computerSelectedRandomNumber:
		print("Guess higher number")
		userInput = int(input("Guess the number again: "))
		
print("The number selected by computer is: ", computerSelectedRandomNumber)
print("Number of attempts: ", count)