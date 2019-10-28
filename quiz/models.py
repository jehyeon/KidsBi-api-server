from django.db import models

class Quiz(models.Model):
  question = models.CharField(max_length=255,default='null')
  url = models.CharField(max_length=255,default='null')
  options = models.CharField(max_length=255,default='null')
  answer = models.IntegerField(default=0)
  category = models.CharField(max_length=50,default='null')
