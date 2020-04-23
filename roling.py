import random
print("Today, we are going to play role the dice.")
a = 1
b = 6
c = print(random.randrange(a, b))
d = input("Do you want to try again?  ")

def whileloop():
	while d == "yes":
		print(c)
	else:
		print('Goodbye.')
whileloop()