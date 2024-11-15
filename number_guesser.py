import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number higher than 0 next time")
        quit()
else:
    print("Please enter a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
print(random_number)

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time.")
