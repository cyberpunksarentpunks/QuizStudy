
import random
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

# used in main
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

# Not used
def ask_question(question, options):
    """
    Function to present a question and return the user's choice.
    
    Args:
    question (str): The question to be asked.
    options (list): List of answer options.
    
    Returns:
    int: The user's chosen option (1, 2, or 3).
    """
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Choose an answer (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")


def quiz_processing():
    # Uses questions dictionaries
    subject = subject_query()
    loaded_data = load_dataset(subject)
    questions = loaded_data

    # Convert dictionary items to a list and shuffle it
    question_list = list(questions.items())
    random.shuffle(question_list)

    score = 0
    
    for question, (options, correct_answer) in question_list:
        user_choice = ask_question(question, options)
        if user_choice == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {options[correct_answer - 1]}.\n")
    
    print(f"Your final score is: {score}/{len(questions)}")


def continue_or_end():
    decision = input("Chcete pokračovat(ano) nebo program ukončit?(ne): ").strip().lower()
    if decision in ["ano", "a", "y", "yes"]:
        return "yes"
    if decision in ["ne", "n", "no"]:
        return "no"
