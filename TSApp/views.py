from django.shortcuts import render

from django.shortcuts import render,redirect
from TSApp import models
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
# def index(request):
#     return render(request,'index.html')
#     #return 'hello world'

# def test(request):
#     print(request.get_full_path())
#     print(request.path)
#     return render(request,'test.html',{"data":100})

# def add(request):
#     a=request.POST.get('a')
#     b=request.POST.get('b')
#     print(a)
#     return render(request,'test.html',{"data":a,"data1":b})

global userid
userid='None'

def check(userinfo,userinfofile):
    userinfofile=open(userinfofile,'r',encoding="utf-8")
    userinfofile=userinfofile.readlines()
    print(userinfo)
    print(userinfofile)
    if (userinfo in userinfofile) or (userinfo+'\n' in userinfofile):
        return 1
    else:
        return 0


    


def login(request):
    return render(request,'login/login.html')

def workplace(request):

    userinfofile='TSApp/user'
    userinfo=str(request.POST.get('userid'))+' '+str(request.POST.get('psword'))
    if check(userinfo,userinfofile):
        global userid
        userid=userinfo.split()[0]
        return render(request,'workplace/workplace.html',{"userid":userid})
    else:
        return render(request,'workplace/workplace.html',{"userid":userid})

    

def selectRoom(request):
    a=request.POST.get('cc')
    print(a)
    return render(request,'selectRoom/selectRoom.html',{"opt":a,"userid":userid})

def selectBed(request):
    return render(request,'selectBed/selectBed.html')

def templateUI(request):
    return render(request,'templateUI/templateUI.html')

def abnormal(request):
    return render(request,'Feedback/Feedback.html')
# Create your views here.
