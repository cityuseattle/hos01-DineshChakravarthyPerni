name = input("Please enter your name:")
guess = input("Please guess a interger between 1 and 6:")
randomNumber = 5
# print("Helllo " + name)

#print("This is your name in all Upper Case: " + name.upper())

#print("This is your name in all Lower case: " + name.lower())

guess = int(guess) # Covert str to int

if(guess == randomNumber):
    print("Congrats, you got it")
else:
    print("OOPS! goodluck next time")