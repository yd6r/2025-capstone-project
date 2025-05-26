import random
from questions_and_answers import basic_python_structures
from questions_and_answers import image_manipulation

def quizzing(subject, random_or_linear):
    percentage_correct = []
    if random_or_linear:
        random.shuffle(subject)
        print("Shuffled!")
    else:
        print("Not shuffling.")
    for item in subject:
        right_answer = item["answers"][0]
        random.shuffle(item["answers"])
        q = input(item["question"] + str(item["answers"]))
        if q.lower() == right_answer:
            print("Correct!")
            percentage_correct.append("correct")
        elif q.lower() != right_answer:
            print("Incorrect.")
            percentage_correct.append("incorrect")
    score = percentage_correct.count("correct") / len(percentage_correct)
    percent_score=str(score).replace("0.", "")
    if percent_score=="1.0":
        percent_score="100"
    elif len(percent_score)==1:
        percent_score+="0"
    print("You got " + str(percent_score)+"% correct.")


while True:
    choose_subject=input("Would you like to be quizzed about basic python structures, or image manipulation?")
    if "basic python structures" in choose_subject.lower():
        choose_random = input("Would you like to shuffle the questions?")
        if choose_random.lower()=="yes":
            quizzing(basic_python_structures, True)
        else:
            quizzing(basic_python_structures, False)

    elif "image manipulation" in choose_subject.lower():
        choose_random = input("Would you like to shuffle the questions?")
        if choose_random.lower()=="yes":
            quizzing(image_manipulation, True)
        else:
            quizzing(image_manipulation, False)

    else:
        print("Invalid reponse.")