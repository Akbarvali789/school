from django.shortcuts import render

# Create your views here.

from app.models import *

def members(request):
    persons=Persons.objects.all().values()
    context={'persons':persons}
    return render(request,'all_persons.html',context)


def details(request,id):
    detail=Persons.objects.get(id=id)
    context={'detail':detail}
    return render(request,'details.html',context)