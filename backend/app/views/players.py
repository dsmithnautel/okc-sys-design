# -*- coding: utf-8 -*-
import logging
from functools import partial
import json
import os

from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from app.dbmodels import models
from django.http import JsonResponse
from django.views import View
from app.models import Player, Game, Shot

LOGGER = logging.getLogger('django')


class PlayerSummary(View):
    logger = LOGGER

    def get(self, request, player_id):
        try:
            player = Player.objects.get(player_id=player_id)
            games = Game.objects.filter(shot__player=player).distinct()
            
            summary = {
                "player_id": player.player_id,
                "name": player.name,
                "team": player.team.name,
                "height": player.height,
                "weight": player.weight,
                "position": player.position,
                "games": []
            }
            
            for game in games:
                shots = Shot.objects.filter(player=player, game=game)
                game_summary = {
                    "game_id": game.game_id,
                    "date": game.date.strftime("%Y-%m-%d"),
                    "home_team": game.home_team.name,
                    "away_team": game.away_team.name,
                    "shots": [
                        {
                            "x": shot.x,
                            "y": shot.y,
                            "made": shot.made
                        } for shot in shots
                    ]
                }
                summary["games"].append(game_summary)
            
            return JsonResponse(summary)
        except Player.DoesNotExist:
            return JsonResponse({"error": "Player not found"}, status=404)
