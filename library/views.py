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

def bookInfo(request):
    print(request.GET)
    return render(request, 'booksinfo.html')

def borrowableBooks(request):
    return render(request, 'borrowablebooks.html')

def returnableBooks(request):
    return render(request, 'returnablebooks.html')

