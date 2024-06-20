from django.db import models
from django.contrib.auth.models import User
from .game import Game


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()
