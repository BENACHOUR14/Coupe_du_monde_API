from django.test import TestCase
from Games.serializers import GamesSerializer
from Games.models import Games
from Teams.models import Teams
from Teams.serializers import TeamSerializer
from Games.tests.factory import GamesFactory
from Teams.tests.factory import TeamsFactory
from faker import Faker

class GameSerializerTestCase(TestCase):
      def test_serializer(self): 
        faker = Faker()  
        team1 = Teams.objects.create(name=faker.pystr(), group=Teams.Group.A)
        team2 = Teams.objects.create(name=faker.pystr(), group=Teams.Group.B)
        game  = GamesFactory.create(date=faker.date(), is_finished=faker.boolean(), stadium=faker.pystr(), home_team=team1,away_team=team2,goal_home_team=faker.random_int(0, 15),goal_away_team=faker.random_int(0, 15))    
        serializer = GamesSerializer(game)
        serializer_home_team = TeamSerializer(game.home_team)
        serializer_away_team = TeamSerializer(game.away_team)
        self.assertEqual(list(serializer.data.keys()), ['id', 'date', 'is_finished', 'stadium', 'home_team', 'away_team', 'goal_home_team', 'goal_away_team'])
        self.assertEqual(str(game.id), serializer.data["id"])
        self.assertEqual(game.date, serializer.data["date"])
        self.assertEqual(game.is_finished, serializer.data["is_finished"])
        self.assertEqual(game.stadium, serializer.data["stadium"])
        self.assertEqual(serializer_home_team.data, serializer.data["home_team"])
        self.assertEqual(serializer_away_team.data, serializer.data["away_team"])
        self.assertEqual(game.goal_home_team, serializer.data["goal_home_team"])
        self.assertEqual(game.goal_away_team, serializer.data["goal_away_team"])
