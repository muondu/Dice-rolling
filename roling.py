import random
import sys

def mycode():
	print("Today, we are going to play role the dice.")
	print("This game gives you random numbers. The first random number is the first dice and the second number is the second dice")

	fistDice = print(random.randrange(1, 6))
	secondDice = print(random.randrange(1, 6))

	d = input("Do you want to try again. Please input yes or no?  ")

	def whileloop():
		while d == "yes":
			mycode()
		else:
			print("Goodbye.")
			sys.exit()
	whileloop()
mycode()