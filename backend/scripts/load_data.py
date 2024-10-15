import json
import os
from django.core.management.base import BaseCommand
from app.models import Player, Team, Game, Shot

class Command(BaseCommand):
    help = 'Load data from JSON files into the database'

    def handle(self, *args, **options):
        self.load_teams()
        self.load_players()
        self.load_games()
        self.load_shots()

    def load_teams(self):
        with open('backend/raw_data/teams.json') as f:
            teams = json.load(f)
        for team in teams:
            Team.objects.get_or_create(
                team_id=team['team_id'],
                defaults={'name': team['name']}
            )

    def load_players(self):
        with open('backend/raw_data/players.json') as f:
            players = json.load(f)
        for player in players:
            team = Team.objects.get(team_id=player['team_id'])
            Player.objects.get_or_create(
                player_id=player['player_id'],
                defaults={
                    'name': player['name'],
                    'team': team,
                    'height': player['height'],
                    'weight': player['weight'],
                    'position': player['position']
                }
            )

    def load_games(self):
        with open('backend/raw_data/games.json') as f:
            games = json.load(f)
        for game in games:
            home_team = Team.objects.get(team_id=game['home_team_id'])
            away_team = Team.objects.get(team_id=game['away_team_id'])
            Game.objects.get_or_create(
                game_id=game['game_id'],
                defaults={
                    'date': game['date'],
                    'home_team': home_team,
                    'away_team': away_team,
                    'home_score': game['home_score'],
                    'away_score': game['away_score']
                }
            )

    def load_shots(self):
        with open('backend/raw_data/shots.json') as f:
            shots = json.load(f)
        for shot in shots:
            player = Player.objects.get(player_id=shot['player_id'])
            game = Game.objects.get(game_id=shot['game_id'])
            Shot.objects.get_or_create(
                shot_id=shot['shot_id'],
                defaults={
                    'player': player,
                    'game': game,
                    'x': shot['x'],
                    'y': shot['y'],
                    'made': shot['made']
                }
            )

# To run this script:
# python manage.py load_data