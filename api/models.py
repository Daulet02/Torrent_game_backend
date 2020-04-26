from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=99)

class Game(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=99)
    description = models.TextField()
    image = models.CharField(max_length=99)
    requirements = models.TextField()