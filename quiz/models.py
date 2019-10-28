from django.db import models

class Quiz(models.Model):
  question: models.CharField(max_length=255)
  url: models.CharField(max_length=255)
  options: models.CharField(max_length=255)
  answer: models.IntegerField()
  category: models.CharField(max_length=50)
