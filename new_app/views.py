from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 

context={
        'random_word':'',
        'attempt':0,
    }
def random_word(request):
    context['random_word']= get_random_string(length=14)
    context['attempt']+=1
    return render(request,'random_word.html',context)
def reset(request):
    print('*'*50)
    print(request.method)
    context['attempt']=0
    return redirect ('/randomword')

# Create your views here.
