from django.shortcuts import render

# Create your views here.

def racha(request):
    d={'name':'racha'}
    return render(request,'racha.html',d)

