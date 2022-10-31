from django.shortcuts import render

from django.shortcuts import render,redirect
from TSApp import models
from django.http import HttpResponse
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return 'hello world'

def test(request):
    print(request.get_full_path())
    print(request.path)
    return render(request,'test.html',{"data":100})

def add(request):
    a=request.POST.get('a')
    b=request.POST.get('b')
    print(a)
    return render(request,'test.html',{"data":100})


def login(request):
    return render(request,'login/login.html')

def workplace(request):
    return render(request,'workplace/workplace.html')

def selectRoom(request):
    return render(request,'selectRoom/selectRoom.html')

def selectBed(request):
    return render(request,'selectBed/selectBed.html')

def templateUI(request):
    return render(request,'templateUI/templateUI.html')

def abnormal(request):
    return render(request,'Feedback/Feedback.html')
# Create your views here.
