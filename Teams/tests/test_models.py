from django.test import TestCase
from Teams.models import Teams
import uuid
from faker import Faker
import pytest
from django.db.utils import IntegrityError

class TeamTestCase(TestCase):
    def test_id_unicity(self):
        faker = Faker()
        team1 = Teams.objects.create(id = uuid.uuid4(), name = faker.pystr(), group = Teams.Group.D)
        with pytest.raises(IntegrityError):
           Teams.objects.create(id = team1.id, name = faker.pystr(), group = Teams.Group.C)
        
    def test_name_length(self):
        faker = Faker()
        team5 = Teams.objects.create(id = uuid.uuid4(), name = faker.pystr(min_chars=51, max_chars=60), group = 'Z')
