from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TboxdSerializer
from .models import Film

# Create your views here.

class FilmView(viewsets.ModelViewSet):
    serializer_class = TboxdSerializer
    queryset = Film.objects.all()