from django.db import models

class Crafts(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()  # No need for max_length in IntegerField
    description = models.TextField(max_length=2000)
    materials = models.CharField(max_length=255)

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5