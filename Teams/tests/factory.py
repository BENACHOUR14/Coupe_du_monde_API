import factory
from faker import Faker
from Teams.models import Teams
import random

faker = Faker()
groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

class TeamsFactory(factory.django.DjangoModelFactory):
    name = factory.LazyFunction(faker.name)
    group = random.choice(groups)
    is_eliminated = faker.boolean()
    
    class Meta:
        model = Teams
