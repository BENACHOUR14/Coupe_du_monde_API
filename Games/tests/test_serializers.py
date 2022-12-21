from django.test import TestCase
from Games.serializers import GamesSerializer
from Games.models import Games
from Teams.models import Teams
from Teams.serializers import TeamSerializer
import datetime

class GameSerializerTestCase(TestCase):
      def test_serializer(self):   
        maroc = Teams.objects.create(name='Maroc', group='H', is_eliminated=False)
        france = Teams.objects.create(name='France', group='A', is_eliminated=False)
        game = Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=maroc, away_team=france)
        serializer = GamesSerializer(game)
        serializer_home_team = TeamSerializer(game.home_team)
        serializer_away_team = TeamSerializer(game.away_team)
        self.assertEqual(list(serializer.data.keys()), ['id', 'date', 'is_finished', 'stadium', 'home_team', 'away_team', 'goal_home_team', 'goal_away_team'])
        self.assertEqual(str(game.id), serializer.data["id"])
        datetest = game.date.strftime("%m/%d/%Y, %H:%M:%S")
        self.assertEqual(datetest, serializer.data["date"])
        self.assertEqual(game.is_finished, serializer.data["is_finished"])
        self.assertEqual(game.stadium, serializer.data["stadium"])
        self.assertEqual(serializer_home_team.data, serializer.data["home_team"])
        self.assertEqual(serializer_away_team.data, serializer.data["away_team"])
        self.assertEqual(game.goal_home_team, serializer.data["goal_home_team"])
        self.assertEqual(game.goal_away_team, serializer.data["goal_away_team"])
