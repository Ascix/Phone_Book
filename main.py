phonebook = {}

def main_menu():
    while 1 == True:
        option = input(f"""Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit

What do you want to do (1-5)? """)
        if option == "1":
            print("\n")
            ask_name = input("What is the person's name? ")
            if ask_name.lower().capitalize() not in phonebook:
                print("There is no entry for that person.\n")
            else:
                print(f"{ask_name.lower().capitalize()}'s number is {phonebook[ask_name.lower().capitalize()]}\n")
        elif option == "2":
            print("\n")
            name = input("What is the person's name? ")
            number = input("What is their phone number? ")
            phonebook[name.lower().capitalize()] = number
            print(f"Entry added for {name.lower().capitalize()}! \n")
        elif option == "3":
            print("\n")
            delete_name = input("What is the person's name? ")
            if delete_name.lower().capitalize() not in phonebook:
                print("There is no entry for that person.\n")
            else:
                del phonebook[delete_name.lower().capitalize()]
                print(f"Entry deleted for {delete_name.lower().capitalize()}! \n")
        elif option == "4":
            print("\n")
            i = [0]
            for i in phonebook:
                print(f"{i}: {phonebook[i]}")
            print("\n")
        elif option == "5":
            print("Closing program. \n")
            exit()
        else:
            print("That is not a valid option! \n")

main_menu()