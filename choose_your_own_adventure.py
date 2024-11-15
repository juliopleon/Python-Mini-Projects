name = input("What is your name")
print("Welcome", name, "to your adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right, which direction would you you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim across? Type walk or swim.")

    if answer == "swim":
        print("You swam across the river and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died.")
    else:
        print("Not a valid option. You are now lost.")

elif answer == "right":
    print("You come to a bridge, it looks wobbly, do you want to cross it or go back? (cross/back) ")

    if answer == "back":
        print("You went back and got lost. You lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them? (yes/no)")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignored the stranger. You lose!")
    else:
        print("Not a valid option. You are now lost.")

else:
    print("Not a valid option. You are now lost.")
