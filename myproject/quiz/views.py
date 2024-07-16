from django.shortcuts import render, redirect
from django.http import HttpResponse
from ...data.ecodata import eco_questions
from ...data.literaturedata import lit_questions

# Create your views here.

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
        subject_query()

def load_dataset(subject):
    if subject == "economy":
        return eco_questions
    elif subject == "literature":
        return lit_questions

def ask_question_view(request):
    if request.method == "POST":
        question_index = int(request.POST.get('question_index'))
        user_choice = int(request.POST.get('choice'))
        score = int(request.POST.get('score'))

        # Check if the answer is correct
        question_key = list(eco_questions.keys())[question_index]
        _, correct_answer = eco_questions[question_key]
        if user_choice == correct_answer:
            score += 1

        # Move to the next question
        question_index += 1
        if question_index >= len(eco_questions):
            return redirect('results', score=score)

        question, (options, correct_answer) = list(eco_questions.items())[question_index]
        return render(request, 'quiz/question.html', {
            'question_index': question_index,
            'question': question,
            'options': options,
            'score': score,
        })
    else:
        # Start the quiz
        question_index = 0
        score = 0
        question, (options, correct_answer) = list(eco_questions.items())[question_index]
        return render(request, 'quiz/question.html', {
            'question_index': question_index,
            'question': question,
            'options': options,
            'score': score,
        })

def results_view(request, score):
    total_questions = len(eco_questions)
    return render(request, 'quiz/results.html', {
        'score': score,
        'total_questions': total_questions,
    })