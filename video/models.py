from django.db import models

class Video(models.Model):
  title = models.CharField(max_length=255)
  source = models.CharField(max_length=255)
  # categories = models.ListCharField(
  #   base_field = models.CharField(max_length=10)
  # )
  categories = models.CharField(max_length=255)
  videoId = models.CharField(max_length=50)
  videoThumbnail = models.CharField(max_length=255)
  videoFile = models.CharField(max_length=1000)
  # like = models.DecimalField()
  likeRatio = models.IntegerField()
  viewCount = models.IntegerField(default=0)
  callCount = models.IntegerField(default=0)
  funSticker = models.IntegerField(default=0)
  notFunSticker = models.IntegerField(default=0)
  updateDate = models.DateTimeField()