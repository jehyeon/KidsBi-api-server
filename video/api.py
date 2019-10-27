from .models import Video
from rest_framework import serializers, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class VideoFilter(django_filters.FilterSet):
  title = django_filters.CharFilter(lookup_expr='icontains')
  categories = django_filters.CharFilter(lookup_expr='icontains')

class VideoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Video
    fields = '__all__'

class VideoViewSet(viewsets.ModelViewSet):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer
  filter_backends = (DjangoFilterBackend,)
  # filter_fields = ('title',)
  filterset_class = VideoFilter