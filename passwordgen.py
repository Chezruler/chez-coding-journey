import random
import string
import os

from time import sleep

def gen_pass(lenght = 12):
    chars = string.ascii_letters + string.digits
    password = ""
    for _ in range(lenght):
        password += random.choice(chars)
    return password

def main():
    while True:
        user_input = input(f"do you want to create a strong password? (Y/N)")
        if user_input.upper() != "Y":
            break
        leng = int(input(f"Enter your password lenght (default is 12)"))
        password = gen_pass(leng)
        print("*****************************************************************")
        print("Copy the password fast, you have 5 seconds before it gets deleted")
        print("*****************************************************************")
        
        sleep(1)
        print("1")
        sleep(1)
        print("2")
        sleep(1)
        print("3")

        print(f"this is your password! it will delete after 5 seconds!")
        print(f"{password}")
        sleep(5)
        os.system('cls')

        


if __name__ == "__main__":
    main()
