# we made this

from rest_framework import serializers   
from .models import Stone

class StoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stone
        fields = ['id','title','description', 'price', 'inventory', 'image']


        # added image for bonus part