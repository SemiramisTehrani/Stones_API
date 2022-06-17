# removing everything here at first and add ours

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def stones_list(request) :

    return Response('ok')

