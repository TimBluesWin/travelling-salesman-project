from django.db import models

class Point(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=120)