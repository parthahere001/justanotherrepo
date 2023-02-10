from django.shortcuts import render,HttpResponse, redirect
from .models import Questions
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateQuestionForm

# Create your views here.
def base(request):
    return render (request,'base.html',context= {'user':User})

def home(request):
    questions = Questions.objects.all()
    context = {'questions': questions}
    if request.user.is_authenticated:
           return render (request,'home.html', context)
    else:
        return render (request,'userlogin.html', context)
    
def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('home')
    else:
        print('USER NOT FOUND')

    context = {}
    return render(request, 'userlogin.html', context)

def finalscore(request):
    questions = Questions.objects.all()
    score_count = 0
    win = False
    total_questions = questions.count()
    for question in questions:
        chosen = request.POST.get(str(question.id))
        if (chosen == question.ans):
            score_count+=1

    if score_count==total_questions:
        win=True
    context = {'score_count': score_count, 'total_questions': total_questions, 'win': win}
    return render (request,'finalscore.html', context)


def createQuestions(request):
    form= CreateQuestionForm()

    if request.method=="POST":
        form=CreateQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context={'form':form}
    return render(request, 'addQuestions.html',context)

def logoutUser(request):
    logout(request)
    return redirect("/")