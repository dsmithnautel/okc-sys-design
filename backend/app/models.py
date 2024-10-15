# -*- coding: utf-8 -*-
from django.db import models

class Team(models.Model):
    team_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)

class Player(models.Model):
    player_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    position = models.CharField(max_length=50)

class Game(models.Model):
    game_id = models.CharField(max_length=50, primary_key=True)
    date = models.DateField()
    home_team = models.ForeignKey(Team, related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_games', on_delete=models.CASCADE)
    home_score = models.IntegerField()
    away_score = models.IntegerField()

class Shot(models.Model):
    shot_id = models.CharField(max_length=50, primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    made = models.BooleanField()
