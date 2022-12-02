from django.shortcuts import render
from django.http import   HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
import datetime

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")