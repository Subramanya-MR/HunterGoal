from django.shortcuts import render
from .models import User

def index(request):
    return render(request, "myapp/index.html",{})

def userreg(request):
    return render(request, "myapp/userreg.html", {})

def index1(request):
    return render(request, "myapp/index1.html",{})

def insertuser(request):
    ffn=request.POST['fn'];
    eei=request.POST['ei'];
    ppn=request.POST['pn'];
    rrg=request.POST['rg'];
    us=User(name=ffn,email=eei,phone_number=ppn,regarding=rrg);
    us.save();
    return render(request, 'myapp/index.html',{})
