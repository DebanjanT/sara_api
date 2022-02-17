from dataclasses import field
from rest_framework import serializers

from api.models import mdl_privateRoom

# Data serializer for sara admin/private room


class SaraPrivateRoom__Serializer__(serializers.ModelSerializer):

    sender = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = mdl_privateRoom
        fields = ['id', 'sender', 'content', 'created_at']
        


