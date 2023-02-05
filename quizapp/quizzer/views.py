from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'home.html')

def quize(request):
    return render (request,'quize.html')