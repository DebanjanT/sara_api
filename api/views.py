from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from api.db_query import DB_get_private_room_info
from api.serializer import SaraPrivateRoom__Serializer__

# api -> views
# Create your views here.

# Getting private room data for sara


@api_view(['GET'])
def sara_private_room(request):
    private_room_info = DB_get_private_room_info  # Complex data
    serializer = SaraPrivateRoom__Serializer__(
        private_room_info, context={'request': request}, many=True)
    return Response(serializer.data)
