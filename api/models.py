from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=99)

class Game(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=99)
    description = models.TextField()
    image = models.CharField(max_length=999)
    requirements = models.TextField()

class Comment(models.Model):
    username = models.CharField(max_length=50)
    text = models.TextField()
    game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE, blank=True)

class Manager(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=2222)