from django.contrib import admin
from .models import *
# # Register your models here.
# class admin1Admin(admin.ModelAdmin):
#     list_display= ("id","adminid","password")
# class studentstudent(admin.ModelAdmin):
#     list_display= ("id","studentid","password")
# class book1book(admin.ModelAdmin):
#     list_display= ("id","bookid","bookname","bookauthor","bookstate")

admin.site.register(admin1)
admin.site.register(student)
admin.site.register(books)