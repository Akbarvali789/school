from django import forms

from student.models import *

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    standard=forms.CharField(max_length=100)
    school=forms.CharField(max_length=100)
    address=forms.CharField(max_length=100)
    email=forms.EmailField()


class Specificstudent(forms.Form):
    name=forms.CharField(max_length=100)
