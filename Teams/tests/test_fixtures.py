from django.test import TestCase
from Teams.models import Teams
from faker import Faker
from django.core.management import call_command

class TeamTestCase(TestCase):  

        def test_existinig_data(self):     
            faker = Faker()
            team1 = Teams.objects.create(name=faker.pystr(), group=Teams.Group.A)
            team2 = Teams.objects.create(name=faker.pystr(), group=Teams.Group.B)
            team3 = Teams.objects.create(name=faker.pystr(), group=Teams.Group.C)
            team4 = Teams.objects.create(name=faker.pystr(), group=Teams.Group.D)
            team5 = Teams.objects.create(name=faker.pystr(), group=Teams.Group.D)
            call_command('fixture_team')
            self.assertEqual(Teams.objects.count(), 4)
            self.assertTrue(Teams.objects.filter(name='Maroc').exists())
            self.assertEqual([t.name for t in Teams.objects.all().order_by('name')], ['Argentine','Croatie','France','Maroc'])
            