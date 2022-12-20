import factory
from faker import Faker
from Games.models import Games
from Teams.tests.factory import TeamsFactory

faker = Faker()

class GamesFactory(factory.django.DjangoModelFactory):
    date=faker.date_time()
    is_finished=faker.boolean()
    stadium = faker.pystr()
    home_team = factory.SubFactory(TeamsFactory)
    away_team = factory.SubFactory(TeamsFactory)
    goal_home_team = faker.random_int(0, 15)
    goal_away_team = faker.random_int(0, 15)
    
    class Meta:
        model = Games
