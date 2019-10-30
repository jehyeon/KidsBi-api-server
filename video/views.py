from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from subprocess import call, check_output
import youtube_dl
import json
# import .models from .

# Create your views here.
def test(request, videoId):
  # temp = Video.objects.all()
  # temp_list = serializers.serialize('json', temp)
  # videoId = 'wFJyfZhxqlU'
  command = 'youtube-dl -f best -g --no-check-certificate http://www.youtube.com/watch?v={0}'.format(videoId)
  url = check_output(command.split()).decode('utf-8').replace('\n', '')
  response = {
    'url': url
  }
  return HttpResponse(json.dumps(response), content_type='application/json')