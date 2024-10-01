from django.db import models
from django.contrib.auth.models import User
import uuid

class Craft(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=2000, default='')
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name