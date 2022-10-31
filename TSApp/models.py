from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

#patient infomation
class SickInfo(models.Model):       
    name=models.CharField(max_length=32) #name
    age=models.IntegerField()   #age
    footnum=models.ImageField() #footnum info(image)
    date=models.DateTimeField() #date
    drug=models.CharField(max_length=128) #drug info
    vein=models.CharField(max_length=1)    #vein choice
    needle=models.CharField(max_length=1)  #needle choice


# Create your models here.
