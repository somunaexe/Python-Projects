import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    answer = input("Do you want to generate a password?\nEnter y for yes or n for no")

    if answer == "yes" or answer == "y":
        length = int(input("How long should the password be : "))
        password = []
        random.shuffle(characters)

        for x in range(length):
            password.append(random.choice(characters))

        random.shuffle(password)
        password = "".join(password)
        print(password)
    elif answer == "no" or answer == "n":
        password = input("Type in your password: ")
        password = "".join(password)
        print("Your password is : ", password)
    else:
        print("Invalid input")
        quit()

generate_password()
    

