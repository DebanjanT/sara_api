from django.urls import path
from api.views import sara_private_room


urlpatterns = [
    path('private-room', sara_private_room, name="private_room")
]
