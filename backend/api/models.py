from django.db import models

class Point(models.Model):
    name = models.CharField(max_length=120)

    def _str_(self):
        return self.title