from django.shortcuts import render

# Create your views here.
def rrr(request):
    d={'name':'RRR'}
    return  render(request,'rrr.html',d)