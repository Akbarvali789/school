from django.shortcuts import render
from django.http import HttpResponse
from student.forms import *
from student.models import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def register(request):
    title = 'Student Registration'
    form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            standard = form.cleaned_data['standard']
            school = form.cleaned_data['school']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            mail=Student.objects.filter(email=email)
            if len(mail)>0:
                 return render(request, 'msg.html', {'title': 'Student  is already exists....try with other email'})
            else:
                
                data = Student(name=name, standard=standard,
                           school=school, address=address, email=email)
                data.save()
                return render(request, 'msg.html', {'title': 'data inserted succesfully'})

    d = {'title': title,
         'form': form}
    return render(request, 'register.html', d)


def existing(request):
    title = 'All Registered Students'
    queryset = Student.objects.all()
    context = {
        'title': title,
        'queryset': queryset
    }
    return render(request, 'existing.html', context)


def search(request):
    title = 'Search Student'
    form = Specificstudent(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        queryset = Student.objects.filter(name=name)
        if len(queryset)==0:
            return render(request, 'msg.html', {'title': 'Student details not found...Please Enter Current Data'})
            

        context = {
        'title': title,
        'queryset':queryset,
        }
        return render(request,'existing.html',context)

    context = {
        'title': title,
        'form' : form,
    }
    return render(request,'search.html',context)



def dropout(request):
    title = 'Drop Out'
    form = Specificstudent(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        queryset = Student.objects.filter(name=name)
        if len(queryset)==0:
            return render(request, 'msg.html', {'title': 'Student details not found...Please Enter Current Data'})
        else:

            queryset = Student.objects.filter(name=name).delete()
            return render(request,'msg.html',{'title':"Student removed from your database"})


    context = {
        'title': title,
        'form' : form,
    }
    return render(request,'search.html',context)
