from django.test import TestCase
from Games.models import Games
from faker import Faker
from django.core.management import call_command
from Games.tests.factory import GamesFactory
from Teams.models import Teams

class GameTestCase(TestCase):
        
    def test_existing_data(self):
        faker = Faker()
        call_command('fixture_team')
        GamesFactory.create_batch(faker.random_int(5, 10))
        call_command('fixture_game')
        self.assertEqual(Games.objects.count(), 2)
        self.assertEqual(Games.objects.filter(away_team=Teams.objects.get(name='France'), home_team=Teams.objects.get(name='Maroc')).count(), 1)
        self.assertTrue(Games.objects.filter(away_team=Teams.objects.get(name='Croatie'), home_team=Teams.objects.get(name='Argentine')).exists())
