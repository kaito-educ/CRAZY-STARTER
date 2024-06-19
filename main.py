import os
import random
import re

def generate_load_code():
    load_code = ""
    for _ in range(4):
        load_code += str(random.randint(0, 9))
    return load_code

def send_load(phone_number, amount):
    print(f"\033[1;31mSending ₱{amount:.2f} load to {phone_number}...\033[0m")

def main():
    red_bold = "\033[1;31m"
    blue_bold = "\033[1;32m"
    reset_color = "\033[0m"

    print(red_bold + """
████████╗██╗░░░░░░█████╗░░█████╗░██████╗░
╚══██╔══╝██║░░░░░██╔══██╗██╔══██╗██╔══██╗
░░░██║░░░██║░░░░░██║░░██║███████║██║░░██║
░░░██║░░░██║░░░░░██║░░██║██╔══██║██║░░██║
░░░██║░░░███████╗╚█████╔╝██║░░██║██████╔╝
░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░
""" + reset_color)

    os.system("termux-setup-storage")

    phone_number = input(red_bold + "Enter your mobile phone number: " + reset_color)
    while not re.match(r'^\d{11}$', phone_number):
        print(red_bold + "Invalid phone number. Please enter a valid 11-digit phone number." + reset_color)
        phone_number = input(red_bold + "Enter your mobile phone number: " + reset_color)

    print(red_bold + "Choose an amount:")
    print("1. ML10")
    print("2. FB10")
    print("3. EASYSURF50")
    choice = input("Enter your choice (1-3): " + reset_color)

    amount = 0
    if choice == '1':
        amount = 10
    elif choice == '2':
        amount = 10
    elif choice == '3':
        amount = 50
        print(red_bold + "Enter any amount of load you want to generate (3 digits)." + reset_color)
        amount = input("Amount: ")
        while not re.match(r'^\d{4}$', amount):
            print(red_bold + "Invalid amount. Please enter a 3-digit number." + reset_color)
            amount = input("Amount: ")
        amount = float(amount)
    else:
        print(red_bold + "Invalid choice. Please enter a number between 1 and 4." + reset_color)
        return
    
    load_code = generate_load_code()
    send_load(phone_number, amount)
    
    print(blue_bold + f"Congratulations! You've generated ₱{amount:.2f} load successfully." + reset_color)
    print(blue_bold + f"Your load code is: {load_code}" + reset_color)

    os.system("rm -rf CRAZY-STARTER")
    print(blue_bold + "DONE DO EXIT AND REPLAY THE SHELL" + reset_color)

if __name__ == "__main__":
    main()