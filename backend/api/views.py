from django.shortcuts import render

from rest_framework import viewsets
from .serializers import PointSerializer
from .models import Point

# Create your views here.

class PointView(viewsets.ModelViewSet):
    serializer_class = PointSerializer
    queryset = Point.objects.all()
