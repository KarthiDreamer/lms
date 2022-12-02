from django.contrib import admin
from .models import *
# Register your models here.
class admin1Admin(admin.ModelAdmin):
    list_display= ("id","adminid","password")
class student1student(admin.ModelAdmin):
    list_display= ("id","studentid","password")
class book1book(admin.ModelAdmin):
    list_display= ("id","bookid","bookname","bookstate")

admin.site.register(admin1,admin1Admin)
admin.site.register(student,student1student)
admin.site.register(books,book1book)