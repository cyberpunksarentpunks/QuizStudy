
import os
import platform
import time
from data.ecodata import eco_questions
from data.literaturedata import lit_questions

def delayed_execution(seconds):
    """
    Function to demonstrate delayed execution.
    """
    # Delay execution for 3 seconds
    time.sleep(seconds)

def clear_screen():
    """
    Clears the terminal screen.
    """
    if platform.system() == "Windows":
        return os.system('cls')
    else:
        return os.system('clear')

# use in main
def subject_query():
    print("Z jakého předmětu se chcete vyzkoušet?: ")
    print("Na výběr z: \n1 - Ekonomie\n2 - Literatura")
    choose_subject = input("Zadej číslo předmětu: ")

    if choose_subject == "1":
        return "economy"
    elif choose_subject == "2":
        return "literature"
    else:
        print("Chyba, zkuste to znovu.")
        delayed_execution(3)
        clear_screen()
        subject_query()
    
def load_dataset(subject):
    if subject == "economy":
        clear_screen()
        return eco_questions
    elif subject == "literature":
        clear_screen()
        return lit_questions


