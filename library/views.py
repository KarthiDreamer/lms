from django.shortcuts import render
from django.http import   HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
import datetime

from django.http import HttpResponse

def home(request):
    return render(request , 'home.html')

def userAuth(request):
    return render(request , 'userauth.html')

def signIn(request):
    return render(request , 'signin.html')

def signUp(request):
    
    return render(request , 'signup.html')

# def bookInfo(request):
#     return render(request , 'booksinfo.html')

def booksInfo(request):
    if request.method == "POST":
        student.studentid
        return render(request, 'booksinfo.html')

def borrowablebooks(request):
    return render(request, 'borrowablebooks.html')

def returnablebooks(request):
    return render(request, 'returnablebooks.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def admindashboard(request):
    return render(request,"admindashboard.html")

def adminaddbook(request):
    return render(request, 'adminaddbook.html')

def adminaddstudent(request):
    return render(request, 'adminaddstudent.html')

