from rest_framework import serializers
from .models import Film

class TboxdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'url')