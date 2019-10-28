from .models import Quiz
from rest_framework import serializers, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class QuizFilter(django_filters.FilterSet):
  category = django_filters.CharFilter(lookup_expr='icontains')

class QuizSerializer(serializers.ModelSerializer):

  class Meta:
    model = Quiz
    fields = '__all__'

class QuizViewSet(viewsets.ModelViewSet):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer
  filter_backends = (DjangoFilterBackend,)
  filterset_class = QuizFilter