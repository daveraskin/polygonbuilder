from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Polygon(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    userName = models.CharField(max_length=100)
    message = models.TextField()
    tags = models.ManyToManyField(Tag)
    color = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.userName}'s Polygon"
