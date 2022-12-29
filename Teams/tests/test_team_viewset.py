from django.test import TestCase,Client
from faker import Faker
from Teams.tests.factory import TeamsFactory
from Teams.models import Teams
from Teams.views import TeamViewSet
from rest_framework import status
from Teams.serializers import TeamSerializer

class TeamViewTest(TestCase):
    
    def test_queryset_serializer(self):
        query_set = TeamViewSet.queryset
        serializer = TeamViewSet.serializer_class
        self.assertEqual(query_set, Teams.objects)
        self.assertEqual(serializer["list"], TeamSerializer)
    
    def test_list(self):
        faker = Faker()
        TeamsFactory.create_batch(faker.random_int(5, 10))
        client = Client()
        response = client.get("/Teams/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Teams.objects.all().count())

    def test_with_name(self):
        team1 = TeamsFactory()
        client = Client()
        response = client.get(f"/Teams/?name={team1.name}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Teams.objects.filter(name=team1.name).count())

        
    def test_with_group(self):
        faker = Faker()
        TeamsFactory.create_batch(faker.random_int(5, 10), group='C')
        TeamsFactory.create_batch(faker.random_int(5, 10), group='A')
        client = Client()
        response = client.get(f"/Teams/?group=C")   
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Teams.objects.filter(group='C').count())
        
    def test_with_is_eliminated(self):
        faker = Faker()
        TeamsFactory.create_batch(faker.random_int(5, 10),is_eliminated=False)
        TeamsFactory.create_batch(faker.random_int(5, 10),is_eliminated=True)
        client = Client()
        response = client.get(f"/Teams/?is_eliminated=False")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Teams.objects.filter(is_eliminated=False).count())

        
    def test_with_search(self):
        team = TeamsFactory(name='Andrea') 
        client = Client()
        namee = team.name[0:3]
        response = client.get(f"/Teams/?search={namee}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Teams.objects.filter(name__startswith=namee).count())
        
        
    def test_retrieve(self):
        teams = TeamsFactory()
        client = Client()
        response = client.get(f'/Teams/{teams.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], str(teams.id))
        
    def test_retrieve_404(self):
        client = Client()
        response = client.get(f'/Teams/0/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_create(self):
        faker = Faker()
        client = Client()
        data = {   
            "name": faker.name(),
            "group": Teams.Group.H,
            "is_eliminated": faker.boolean()
        }
        response = client.post(
            "/Teams/",
            data=data,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Teams.objects.filter(pk=response.json()['id']).count(), 1)
        
    def test_update(self):
        faker = Faker()
        team = TeamsFactory()
        data = {
            "name": faker.name(),
            "group": team.group,
            "is_eliminated": team.is_eliminated
            }
        response = self.client.put(f'/Teams/{team.id}/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        team.refresh_from_db()
        self.assertEqual(team.name, data['name'])
