from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('hello world....')

def sec(request):
    return render(request,'sec.html')