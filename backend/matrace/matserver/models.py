from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    number = models.CharField(max_length = 50)
    description = models.CharField(max_length = 250, blank=True, null=True)
    manufacturer = models.CharField(max_length = 50, blank=True, null=True)
    provider = models.CharField(max_length = 50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.number

class Carrier(models.Model):
    uid = models.CharField(max_length = 50)
    description = models.CharField(max_length = 250, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.description