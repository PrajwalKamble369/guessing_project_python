import random
number = random.randint(20,50)
guess_number = int(input("Enter a Number"))

if guess_number == number:
    print("Congarts You won")

else:
    print("Sorry try again")
    for i in range(3):
        guess_number = int(input("Guess Number"))
        if guess_number == number:
            print("Write guess")

            break

        else:
            print("You won")

        