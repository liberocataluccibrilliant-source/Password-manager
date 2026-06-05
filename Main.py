"""Main"""


"""Imports"""
import os
import json
import random
import time
import itertools
import string
"""System variables"""
file_name = "Passwords.json" #if you want to use this code just change the line with the file name you prefer
passwords = {}
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
"""Functions"""
#FOR SEPARTE CONTENTS
def separator():
    character = "-"
    try:
        length = os.get_terminal_size().columns
    except OSError:
        length = 80
    
    print(character * length)

#FOR WELCOME AT THE START OF THE PROGRAMM
def welcome():
    separator()
    print(r"""
    ____                                          __   __  ___                                 
   / __ \____ ____________      ______  _________/ /  /  |/  /___ _____  ____ _____ ____  _____
  / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  /  / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ ___/
 / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /  / /  / / /_/ / / / / /_/ / /_/ /  __/ /    
/_/    \__,_/____/____/ |__/|__/\____/_/   \__,_/  /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                                                                            /____/             """)
    separator()
#FOR ADD A PASSWORD (to a dictionary)
def add_password(dictionary=None):
    service = input("Type the name of the service (EX: Discord, Roblox, GitHub): ")
    username = input("Type the username: ")
    password = input("Type the password: ")
    try:
        dictionary[service] = {
            "username": username,
            "password": password
        }
        print("Password added!")
    except Exception as Error:
        print(f"ERROR while saving the passwords ({Error})")

    return dictionary

#FOR WRITE THE PASSWORDS IN THE FILE
def write_passwords(dictionary=None, path=str):
    if type(dictionary) != dict:
        print("ERROR: parameter not a dict!")
    else:
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, "r") as file:
                passwords_found = json.load(file)
        else:
            passwords_found = {}
    passwords_found.update(dictionary)
    with open(path, "w") as file:
        json.dump(passwords_found, file, indent=4)
    
    return passwords_found

                    
#FOR READ THE ALL PASSWORDS
def load_passwords(path=str, dictionary=None):
    if os.path.exists(path):
        if os.path.getsize(path) > 0:
            with open(path, "r") as file:
                passwords_found = json.load(file)
            for service, data in passwords_found.items():
                print(f"Service: {service}")
                print(f"  |- Username: {data['username']}")
                print(f"  |- Password: {data['password']}")
                separator()
        else:
            try:
                for service, data in dictionary.items():
                    print(f"Service: {service}")
                    print(f"  |- Username: {data['username']}")
                    print(f"  |- Password: {data['password']}")
                    separator()
            except:
                print("ERROR!")
    else:
        print("ERROR: file doesn't exist!. Creating it now...")
        try:
            with open(path, "w") as file:
                pass
        except Exception as Error:
            print(f"ERROR: {Error}")

#FOR SEARCH A PASSWORD
def searchPassword(path=str, dictionary=None):
    print("[1] for search by NAME OF THE SERVICE")
    print("[2] for search by USERNAME")
    action = input("Type a number: ")
    if action == "1":
        service_name = input("Type the name of the service: ")
        try:
            with open(path, "r") as file:
                passwords_found = json.load(file)
            if service_name in passwords_found:
                data = passwords_found[service_name]
                print(f"Service: {service_name}")
                print(f"  |- Username: {data['username']}")
                print(f"  |- Password: {data['password']}")
                separator()
            else:
                print("ERROR: not found!")
        except Exception as Error:
            print(f"ERROR while searching password ({Error})")
    elif action == "2":
        username = input("Type the username: ")
        if not os.path.exists(path):
            print("ERROR: file not found! Creating it right now...")
            try:
                with open(path, "w") as file:
                    pass
                print("File created!")
            except Exception as Error:
                print(f"ERROR: {Error}")
        else:
            if os.path.getsize(path) == 0:
                print("ERROR: file empty!")
            else:
                with open(path, "r") as file:
                    passwords_found = json.load(file)
                for key, value in passwords_found.items():
                    if username == value["username"]:
                        print(f"Service: {key}")
                        print(f"  |- Username: {value['username']}")
                        print(f"  |- Password: {value['password']}")
                        separator()
                        found = True
                if not found:
                    print("Not found!")
                    
            
#FOR DELETE A PASSWORD
def deletePassword(dictionary=None, path=str):
    load_passwords(path, dictionary)
    service_ToDelete = input("Type the name of the service that the password you want to delete is associated with: ")
    password_ToDelete = input("Type the password that you want to delete (which is associated with the service typed before): ")
    try:
        with open(path, "r") as file:
            passwords_found = json.load(file)
    except Exception as Error:
        print(f"ERROR: {Error}")
    to_delete = []
    for key, value in passwords_found.items():
        if key == service_ToDelete and value["password"] == password_ToDelete:
            to_delete.append(service_ToDelete)
    request = input("Do you want to delete this passwords? [Y/n]").lower()
    if request == "y":
        for _ in to_delete:
            del passwords_found[_]
            print("Password deleted!")
        dictionary = passwords_found
        print(dictionary)
        with open(path, "w") as file:
         json.dump(passwords_found, file, indent=1)
    else:
        print("Operation aborted!")


#FOR GENERATE A PASSWORD
def generatePassword():
    try:
        allowed = True
        length = int(input("How long should the password be?: "))
        result = ""
        if length > 20:
            request = input("Length bigger than 20. Are you sure you want to continue? [Y/n]: ").lower()
            if request == "y":
                allowed = True
            else:
                print("Operation aborted!")
                allowed = False
        if allowed:
            for i in range(length):
                character = random.choice(characters)
                result = result + character
            else:
                print(f"Random password: {result}")
    except ValueError:
        print("ERROR: invalid number!")

#FOR TEST A PASSWORD
def test_password():
    password = input("Type the password to test: ")
    alphabet = string.ascii_letters + string.digits + string.punctuation
    start = time.time()
    for length in range(1, len(password) + 1):
        for attempt in itertools.product(alphabet, repeat=length):
            attempt = ''.join(attempt)
            if attempt == password:
                end = time.time()
                print(f"\nPassword found: {attempt}")
                print(f"Time taken: {end - start:.4f} seconds")
            else:
                print("Password not guessed!")

#FOR SHOW THE MENU
def show_menu():
    print("[1] for add a password")
    print("[2] for see all the passwords")
    print("[3] for search a password")
    print("[4] for delete a password")
    print("[5] for generate a random password")
    print("[6] for test the password strength")
    print("[7] for exit")

#FOR CLEAN THE TERMINAL
def clean():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        separator()
"""Script"""
welcome()
while True:
    separator()
    show_menu()
    action = input("Type a number: ")
    if action == "1":
        add_password(passwords)
        write_passwords(passwords, file_name)
    elif action == "2":
        load_passwords(file_name, passwords)
    elif action == "3":
        searchPassword(file_name, passwords)
    elif action == "4": 
        deletePassword(passwords, file_name)
    elif action == "5":
        generatePassword()
    elif action == "6":
        test_password()
    elif action == "7":
        print("Closing the programm...")
        break
    else:
        print("Invalid number!")
        clean()