from django.shortcuts import render

# Create your views here.

def name(request):
    d={'name':'akbar','age':21}
    return render(request,'name.html',d)


