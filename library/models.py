from django.db import models

class student(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    studentid= models.CharField(max_length=100)


