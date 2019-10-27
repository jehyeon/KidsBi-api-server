from django.db import models

class Category(models.Model):
  videoCategory = models.CharField(max_length=50)
  imageURL = models.CharField(max_length=255)