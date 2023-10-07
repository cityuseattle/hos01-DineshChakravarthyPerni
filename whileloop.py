attempts = 0
randomNumber = 5

while attempts < 3: 
    guess = input("Please guess an integer between 1 and 6:")
    guess = int(guess)  # Convert str to int

    if guess == randomNumber:
        print("Congrats, you got it")
        break  
    else:
        print("OOPS! Good luck next time")
        attempts += 1

if attempts == 3:
    print("You've used all your attempts.")
