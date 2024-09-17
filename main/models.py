from django.db import models
import uuid

class Craft(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=2000, default='')

    def __str__(self):
        return self.name