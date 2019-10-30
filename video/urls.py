from django.urls import path
from . import views

urlpatterns = [
  path('<videoId>', views.test, name='test')
]