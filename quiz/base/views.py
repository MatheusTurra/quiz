from django.shortcuts import render
from quiz.base.models import Questions 

def home(request):
    return render(request, "base/home.html")

def questions(request, index):
    question = Questions.objects.filter(available=True).order_by("id")[index - 1]
    context = {"index": index, "Question": question}
    print(question)
    return render(request, "base/game.html", context=context)

def leaderboards(request):
    return render(request, "base/leaderboards.html")