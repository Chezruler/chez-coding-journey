import string
import os
import secrets

from time import sleep

def main():
    while True:
        user_input = input(f"do you want to create a strong password? (Y/N)")
        if user_input.upper() != "Y":
            break
        leng = int(input(f"Enter your password lenght (default is 12)"))
        password = secrets.token_hex(leng)
        print("*****************************************************************")
        print("Copy the password fast, you have 5 seconds before it gets deleted")
        print("*****************************************************************")
        
        for i in range(3):
            sleep(1)
            print(i + 1)

        print(f"this is your password! it will delete after 5 seconds!")
        print(f"{password}")
        sleep(5)
        os.system('cls')

        


if __name__ == "__main__":
    main()
