from django.db import models


# Create your models here.
class mdl_publicRoom(models.Model):
    # user
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
