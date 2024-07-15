# main.py

import random
from data.ecodata import eco_questions
from data.literaturedata import lit_questions
from modules.intro import subject_query, load_dataset 
from modules.intro import clear_screen
from modules.outro import continue_or_end

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


def main():
    # Use eco_questions dictionary
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


if __name__ == "__main__":
    run = True
    while run == True:
        main()
        cont = continue_or_end()
        if cont == "no":
            run == False
            exit()
