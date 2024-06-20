from django.db import models
from django.contrib.auth.models import User
from .category import Category
from .game import Game


class GameCategory(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
