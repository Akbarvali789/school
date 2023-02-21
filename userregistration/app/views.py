from django.shortcuts import render

# Create your views here.

def SignupPage(request):
    return render(request,'signup.html')