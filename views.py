from django.shortcuts import render
from random import randint

# Create your views here.

def home(request):
    return render(request, "flashCard/home.html")

def add(request):
    num1 = randint(0,10)
    num2 = randint(0,10)

    if request.method=="POST":
        answer = request.POST["answer"]
        old_num1 = request.POST["old_num1"]
        old_num2 = request.POST["old_num2"]

        if not answer:
            return render(request, "flashCard/add.html", {
                                     'num1': num1,
                                     'num2': num2,
                                                 })

        correct_answer = int(old_num1) + int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "correct "  + "   " + old_num1 + "+" + old_num2 + "=" + answer
            color ="success"
        else :
            my_answer = "incorrect "  + "   " + old_num1 + "+" + old_num2 + "+"  " is not " + answer + "  it is  " + str(correct_answer)
            color ="danger"

        return render(request, "flashCard/add.html", {'answer' : answer,
                                                      'my_answer' : my_answer, 
                                                      'num1': num1, 
                                                      'num2': num2, 
                                                      'color': color })
    return render(request, "flashCard/add.html", {
        'num1': num1,
        'num2': num2,
    })

def subtract(request):
    num1 = randint(0,10)
    num2 = randint(0,10)

    if request.method=="POST":
        answer = request.POST["answer"]
        old_num1 = request.POST["old_num1"]
        old_num2 = request.POST["old_num2"]

        if not answer:
            return render(request, "flashCard/subtract.html", {
                                     'num1': num1,
                                     'num2': num2,
                                                 })

        correct_answer = int(old_num1) - int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "correct answer!!!"  + "   " + old_num1 + "-" + old_num2 + "=" + answer
            color ="success"
        else :
            my_answer = "incorrect answer"  + "   " + old_num1 + "-" + old_num2 +  " is not " + answer + "  it is  " + str(correct_answer)
            color ="danger"

        return render(request, "flashCard/subtract.html", {'answer' : answer,
                                                      'my_answer' : my_answer, 
                                                      'num1': num1, 
                                                      'num2': num2, 
                                                      'color': color })
    return render(request, "flashCard/subtract.html", {
        'num1': num1,
        'num2': num2,
    })

def multiply(request):
    num1 = randint(0,10)
    num2 = randint(0,10)

    if request.method=="POST":
        answer = request.POST["answer"]
        old_num1 = request.POST["old_num1"]
        old_num2 = request.POST["old_num2"]

        if not answer:
            return render(request, "flashCard/multiply.html", {
                                     'num1': num1,
                                     'num2': num2,
                                                 })

        correct_answer = int(old_num1) * int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "correct answer!!!"  + "   " + old_num1 + "*" + old_num2 + "=" + answer
            color ="success"
        else :
            my_answer = "incorrect answer"  + "   " + old_num1 + "*" + old_num2 +  " is not " + answer + "  it is  " + str(correct_answer)
            color ="danger"

        return render(request, "flashCard/multiply.html", {'answer' : answer,
                                                      'my_answer' : my_answer, 
                                                      'num1': num1, 
                                                      'num2': num2, 
                                                      'color': color })
    return render(request, "flashCard/multiply.html", {
        'num1': num1,
        'num2': num2,
    })


def divide(request):
    num1 = randint(0,10)
    num2 = randint(1,10)

    if request.method=="POST":
        answer = request.POST["answer"]
        old_num1 = request.POST["old_num1"]
        old_num2 = request.POST["old_num2"]

        if not answer:
            return render(request, "flashCard/divide.html", {
            'answer':answer,
            'num1': num1,
            'num2': num2,
            })

        correct_answer = int(old_num1) / int(old_num2)
        if float(answer) == correct_answer:
            my_answer = "correct"  + "   " + old_num1 + "/" + old_num2 + "=" + answer
            color ="success"
        else :
            my_answer = "incorrect"  + "   " + old_num1 + "/" + old_num2 +  " is not " + answer + "  it is  " + str(correct_answer)
            color ="danger"

        return render(request, "flashCard/devide.html", {'answer' : answer,
                                                      'my_answer' : my_answer, 
                                                      'num1': num1, 
                                                      'num2': num2, 
                                                      'color': color })
    return render(request, "flashCard/divide.html", {
        'num1': num1,
        'num2': num2,
    })