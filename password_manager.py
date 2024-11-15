master_pwd = input("What is the master password? ")


def view():
    pass


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd)


while True:
    mode = input(
        "Would you like to add a new password or view existing passwords (view/add), press q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        view()
    else:
        print("Invalid mode.")
        continue
