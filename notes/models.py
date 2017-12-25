from django.db import models
from django.conf import settings


# Create your models here.


class Note(models.Model):
    label = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="notes_owner", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
