from django.test import TestCase,Client
from faker import Faker
from Games.tests.factory import GamesFactory
from Games.models import Games
from Games.views import GameViewSet
from rest_framework import status
from Games.serializers import GamesSerializer

class GameViewTest(TestCase):
    
    def test_queryset_serializer(self):
        query_set = GameViewSet.queryset
        serializer = GameViewSet.serializer_class
        self.assertEqual(query_set, Games.objects)
        self.assertEqual(serializer["list"], GamesSerializer)
            
    def test_list(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10))
        client = Client()
        response = client.get("/Games/")
        self.assertEqual(len(response.json()), Games.objects.all().count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_with_date(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10))
        game = GamesFactory(date='2022-11-28T14:36:38.146211Z')
        client = Client()
        response = client.get(f"/Games/?kw=date&value={game.date}")
        print(len(response.data))
        print(Games.objects.all().count())
        self.assertEqual(len(response.json()), Games.objects.filter(date=game.date).count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_with_is_finished(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10), is_finished=False)
        GamesFactory.create_batch(faker.random_int(5, 10), is_finished=True)
        client = Client()
        response = client.get(f"/Games/?kw=is_finished&value=False")
        self.assertEqual(len(response.json()), Games.objects.filter(is_finished=False).count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_with_stadium(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10), stadium='Maracana')
        GamesFactory.create_batch(faker.random_int(5, 10))
        client = Client()
        response = client.get(f"/Games/?kw=stadium&value=Maracana")
        self.assertEqual(len(response.json()), Games.objects.filter(stadium='Maracana').count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
            
    def test_home_team(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10))
        game = GamesFactory()
        client = Client()
        response = client.get(f"/Games/?kw=home_team&value={game.home_team.id}")
        self.assertEqual(len(response.json()), Games.objects.filter(home_team=game.home_team).count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_away_team(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10))
        game = GamesFactory()
        client = Client()
        response = client.get(f"/Games/?kw=away_team&value={game.away_team.id}")
        self.assertEqual(len(response.json()), Games.objects.filter(away_team=game.away_team).count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_retrieve(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10))    
        game = GamesFactory()
        client = Client()
        response = client.get(f'/Games/{game.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], str(game.id))
        
    def test_retrieve_404(self):
        client = Client()
        response = client.get(f'/Games/0/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
