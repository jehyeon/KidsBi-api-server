from django.urls import path
from . import views

urlpatterns = [
  path('randomVideos/', views.randomVideos, name='randomVidoes'),
  path('video/<videoId>', views.convertId, name='convertId')
]