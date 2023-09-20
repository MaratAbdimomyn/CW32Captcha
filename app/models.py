from django.db import models

class Planets(models.Model):
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=40)

    def __str__(self):
        return self.models_name