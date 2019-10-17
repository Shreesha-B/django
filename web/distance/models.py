from django.db import models


class Cords(models.Model):
    latitude = models.FloatField(default=0)
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=1000)
    longitude = models.FloatField(default=0)
    dis = models.FloatField(default=0)

    def __str__(self):
        return self.name




