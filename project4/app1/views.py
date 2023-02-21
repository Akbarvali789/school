from django.shortcuts import render

#Create your views here.

def orange(request):
    d={'name':'orange'}
    return render(request,'orange.html',d)