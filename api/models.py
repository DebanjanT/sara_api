from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.


class mdl_privateRoom(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_by")
    content = models.CharField(max_length=500, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
