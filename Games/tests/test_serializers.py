from django.test import TestCase
from Games.serializers import GamesSerializer
from Teams.models import Teams
from Teams.serializers import TeamSerializer
from Games.tests.factory import GamesFactory
from faker import Faker
import uuid
from Teams.tests.factory import TeamsFactory

class GameSerializerTestCase(TestCase):
      def test_serializer(self): 
        faker = Faker()  
        team1 = Teams.objects.create(name=faker.pystr(), group=Teams.Group.A)
        team2 = Teams.objects.create(name=faker.pystr(), group=Teams.Group.B)
        serializer_home_team = TeamSerializer(team1)
        serializer_away_team = TeamSerializer(team2)
        game  = GamesFactory.create(date=faker.date(), is_finished=faker.boolean(), stadium=faker.pystr(), home_team=team1, away_team=team2, goal_home_team=faker.random_int(0, 15), goal_away_team=faker.random_int(0, 15))    
        serializer = GamesSerializer(game)
        self.assertEqual(list(serializer.data.keys()), ['id', 'date', 'is_finished', 'stadium', 'home_team', 'away_team', 'goal_home_team', 'goal_away_team'])
        self.assertEqual(str(game.id), serializer.data["id"])
        self.assertEqual(game.date, serializer.data["date"])
        self.assertEqual(game.is_finished, serializer.data["is_finished"])
        self.assertEqual(game.stadium, serializer.data["stadium"])
        self.assertEqual(str(game.home_team.id), serializer_home_team.data['id'])
        self.assertEqual(str(game.away_team.id), serializer_away_team.data["id"])
        self.assertEqual(game.goal_home_team, serializer.data["goal_home_team"])
        self.assertEqual(game.goal_away_team, serializer.data["goal_away_team"])
        
      def test_serializer_required(self):
        serializer = GamesSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("date")[0].code, "required")
        self.assertEqual(serializer.errors.get("stadium")[0].code, "required")
        self.assertEqual(serializer.errors.get("home_team")[0].code, "required")
        self.assertEqual(serializer.errors.get("away_team")[0].code, "required")
        
      def test_serializer_blank_fields(self):
        serializer = GamesSerializer(data={'date':'', 'is_finished':'', 'stadium':'', 'home_team':{'id':'', 'name':'', 'group':'', 'is_eliminated':''}, 'away_team':{'id':'', 'name':'', 'group':'', 'is_eliminated':''}, 'goal_home_team':'', 'goal_away_team':''})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("date")[0].code, "invalid")
        self.assertEqual(serializer.errors.get("is_finished")[0].code, "invalid")
        self.assertEqual(serializer.errors.get("stadium")[0].code, "blank")
        self.assertEqual(serializer.errors.get("home_team")[0].code, "invalid")
        self.assertEqual(serializer.errors.get("goal_home_team")[0].code, "invalid")
        self.assertEqual(serializer.errors.get("goal_away_team")[0].code, "invalid")
            
      def test_invalid_fields(self):
        serializer = GamesSerializer(data={'date':'27/12/2022', 'stadium':'randomstadium', 'home_team':{'id':uuid.uuid4(), 'name':'Test', 'group':'Z', 'is_eliminated':'not_boolean'}, 'away_team':{'id':uuid.uuid4(), 'name':'Test2', 'group':'X', 'is_eliminated':'not_boolean'}, 'goal_home_team':'XX', 'goal_away_team':'YY'})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("date")[0].code, "invalid")
        self.assertEqual(serializer.errors.get("home_team")[0].code, "invalid")
        self.assertEqual(serializer.errors.get("away_team") [0].code, "invalid")
        self.assertEqual(serializer.errors.get("goal_home_team")[0].code, "invalid")
        self.assertEqual(serializer.errors.get("goal_away_team")[0].code, "invalid")
