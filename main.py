
from modules.processes import *


def main():
    subject = subject_query()
    loaded_data = load_dataset(subject)
    questions = loaded_data
    quiz_processing()
    #ask_question(questions)
    


if __name__ == "__main__":
    run = True
    while run == True:
        clear_screen()
        main()
        cont = continue_or_end()
        if cont == "no":
            run == False
            exit()
