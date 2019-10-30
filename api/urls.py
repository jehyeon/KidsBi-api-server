"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

# Importing models
import video.api
import category.api
import quiz.api

videoRouter = routers.DefaultRouter()
categoryRouter = routers.DefaultRouter()
quizRouter = routers.DefaultRouter()

videoRouter.register('videos', video.api.VideoViewSet)
categoryRouter.register('categories', category.api.CategoryViewSet)
quizRouter.register('quizzes', quiz.api.QuizViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include((videoRouter.urls, 'video'), namespace='video')),
    url(r'^api/', include((categoryRouter.urls, 'category'), namespace='category')),
    url(r'^api/', include((quizRouter.urls, 'quiz'), namespace='quiz')),
    url(r'^convert/', include('video.urls'))
]
