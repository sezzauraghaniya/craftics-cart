from django.db import models

class Craft(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name