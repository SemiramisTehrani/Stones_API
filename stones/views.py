# removing everything here at first and add ours

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StoneSerializer
from .models import Stone
from stones import serializers


@api_view(['GET','POST'])
def stones_list(request) :
    
    if request.method == 'GET' :
        stones = Stone.objects.all()
        serializer = StoneSerializer(stones, many = True)
        return Response(serializer.data)

    elif request.method == 'POST' :
         serializer = StoneSerializer(data = request.data)
         serializer.is_valid(raise_exception = True)
         serializer.save()
         return Response(serializer.data, status = status.HTTP_201_CREATED)
 
@api_view(['GET'])
def stone_detail(request, pk) :
    try :
        stone = Stone.objects.get(pk=pk)
        serializer = StoneSerializer(stone);
        return Response(serializer.data)

    except Stone.DoesNotExist :
        return Response(status = status.HTTP_404_NOT_FOUND)







    
    