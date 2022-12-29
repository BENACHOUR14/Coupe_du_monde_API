from django.test import TestCase,Client
from faker import Faker
from Games.tests.factory import GamesFactory
from Games.models import Games
from Games.views import GameViewSet
from rest_framework import status
from Games.serializers import GamesSerializer
import uuid

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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Games.objects.all().count())
        
    def test_with_date(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10))
        game = GamesFactory(date='2022-11-28T14:36:38.146211Z')
        client = Client()
        response = client.get(f"/Games/?date={game.date}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Games.objects.filter(date=game.date).count())
        
    def test_with_is_finished(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10), is_finished=False)
        GamesFactory.create_batch(faker.random_int(5, 10), is_finished=True)
        client = Client()
        response = client.get(f"/Games/?is_finished=False")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Games.objects.filter(is_finished=False).count())
        
    def test_with_stadium(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10), stadium='Maracana')
        GamesFactory.create_batch(faker.random_int(5, 10))
        client = Client()
        response = client.get(f"/Games/?stadium=Maracana")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Games.objects.filter(stadium='Maracana').count())
       
    def test_home_team(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10))
        game = GamesFactory()
        client = Client()
        response = client.get(f"/Games/?home_team={game.home_team.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Games.objects.filter(home_team=game.home_team).count())
        
    def test_away_team(self):
        faker = Faker()
        GamesFactory.create_batch(faker.random_int(5, 10))
        game = GamesFactory()
        client = Client()
        response = client.get(f"/Games/?away_team={game.away_team.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Games.objects.filter(away_team=game.away_team).count())
        
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
        
    # def test_create(self):
    #     faker = Faker()
    #     client = Client() 
    #     data={
    #             'date':'27/12/2022',
    #             'is_finished':False,
    #             'stadium':'randomstadium',
    #             'home_team':{'id':uuid.uuid4(),
    #                          'name':'Test',
    #                          'group':'A',
    #                          'is_eliminated':False},
    #             'away_team':{'id':uuid.uuid4(),
    #                         'name':'Test2',
    #                          'group':'B',
    #                          'is_eliminated':False},
    #             'goal_home_team':0,
    #             'goal_away_team':0
    #         }
    #     response = client.post(
    #         "/Games/",
    #         data=data,
    #         content_type="application/json",
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Games.objects.filter(pk=response.json()['id']).count(), 1)

    # def test_update(self):
    #     faker = Faker()
    #     game = GamesFactory()
    #     data = {
    #             'date':'27/12/2022',
    #             'is_finished':False,
    #             'stadium':'randomstadium',
    #             'home_team':{'id':uuid.uuid4(),
    #                          'name':'Test',
    #                          'group':'A',
    #                          'is_eliminated':False},
    #             'away_team':{'id':uuid.uuid4(),
    #                         'name':'Test2',
    #                          'group':'B',
    #                          'is_eliminated':False},
    #             'goal_home_team':0,
    #             'goal_away_team':0
    #         }
    #     response = self.client.put(f'/Games/{game.id}/', data=data, content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     game.refresh_from_db()
    #     self.assertEqual(game.date, data['date'])
