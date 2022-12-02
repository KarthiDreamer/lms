from django.db import models

class student(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    studentid= models.CharField(max_length=100 ,null=True)
    password=models.CharField(max_length=100 , null=True)

class admin1(models.Model):
    id=models.AutoField(primary_key=True,unique=True,)
    adminid= models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class books(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    bookid=models.CharField(max_length=100)
    bookname=models.CharField(max_length=100)
    bookauthor=models.CharField(max_length=100, null=True)
    bookstate=models.BooleanField()

