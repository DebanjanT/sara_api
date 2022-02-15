from django.http import JsonResponse
from django.shortcuts import render
from api.db_constant import DB_get_public_room_info

# api -> views
# Create your views here.


def public_room(request):
    public_room_info = DB_get_public_room_info
    return JsonResponse({
        'public_room': public_room_info
    })
