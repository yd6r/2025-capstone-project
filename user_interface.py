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
        print(item["question"])
        random.shuffle(item["answers"])
        times_run=0
        for i in item["answers"]:
            times_run+=1
            print(str(times_run) + ") " + i)
            
        q = input()
        if q.isdigit():
            index_answer = int(q)-1
            if index_answer < 0 or index_answer >= len(item["answers"]):
                print("Index out of range, marked as incorrect. The correct answer was " + right_answer)
                percentage_correct.append("incorrect")
            elif item["answers"][index_answer] == right_answer:
                print("Correct!")
                percentage_correct.append("correct")
            else:
                print("Incorret. The correct answer was " + right_answer)
                percentage_correct.append("incorrect")
        else: # q is not a digit
            print("invalid input")
            percentage_correct.append("incorrect")
    score = percentage_correct.count("correct") / len(percentage_correct)
    percent_score=str(score).replace("0.", "")
    if percent_score=="1.0":
        percent_score="100"
    elif len(percent_score)==1:
        percent_score+="0"
    print("You got " + str(percent_score)+"% correct.")


while True:
    choose_subject=input("Would you like to be quizzed about: 1) basic python structures, or 2) image manipulation?\n")
    if choose_subject=="1":
        print("You have selected 'basic python structures'")
        choose_random = input("Would you like to shuffle the questions?(y/N)\n")
        if choose_random.lower()=="y":
            quizzing(basic_python_structures, True)
        else:
            quizzing(basic_python_structures, False)

    elif choose_subject=="2":
        print("You have selected 'image manipulation'")
        choose_random = input("Would you like to shuffle the questions?(y/N)\n")
        if choose_random.lower()=="y":
            quizzing(image_manipulation, True)
        else:
            quizzing(image_manipulation, False)

    else:
        print("Invalid reponse.")
