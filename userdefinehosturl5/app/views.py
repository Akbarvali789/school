from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hai(request):
    return HttpResponse('hai this is by hostbase url')