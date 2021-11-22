import name_generator as gen
import os
import pdb

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def get_user_data():
    name = input("\nWhat is your name?\n").lower()
    if (name == "exit"): return name
    month = input("\nWhat is your birth month? (please type full name e.g. January)\n").lower()
    if (month == "exit"): return month
    return (name, month)

def get_option():
    option = input("\nWhat kind of name do you want? (Choose 'dragon' or 'penguin')\n").lower()
    return option

def handle_option(user_data, option):
    name, month = user_data
    if (option == "dragon"):
        result = gen.dragon.get_dragon_name(name, month)
    elif (option == "penguin"):
        result = gen.penguin.get_penguin_name(name, month)
    else:
        result = "none"
        
    return result


def run():
    clear_screen()
    print("\nWelcome to our name generator, type 'exit' at any point to stop!\n")
    try:
        while(True):
            user_data = get_user_data()
            if (user_data == "exit"): break

            option = get_option()
            if (option == "exit"): break

            result = handle_option(user_data, option)
            clear_screen()
            print(f"Your {option} name is {result}")
    except Exception:
        print("\nTerribly sorry, there's been an error!\n")
    finally:
        print("\nThanks for using our name generator!\n")

if __name__ == "__main__":
    run()
