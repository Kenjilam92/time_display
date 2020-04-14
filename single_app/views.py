from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
def homepage(request):
    context ={
        'time': strftime('%Y-%m-%d %H:%M %p',gmtime())
    }
    return render(request,'homepage.html',context)
# Create your views here.
