from django.db import models
# Create your models here.

class Library(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    description = models.CharField(max_length=400)
    def __str_(self):
        return "Library for {}".format(self.name)