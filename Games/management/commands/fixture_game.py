from django.core.management.base import BaseCommand
from Games.models import Games
from Teams.models import Teams
import datetime

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        help = 'Insert two games as fixtures'
        self.load_Games()
                   
    def load_Games(self):
        Games.objects.all().delete()
        maroc = Teams.objects.get(id='77667fbe1aca4126b7104c3c3b725e8a')
        france = Teams.objects.get(id='f9fe63225619405b88ec2166c3a95d53')
        argentine = Teams.objects.get(id='4014ab70a68e47bb899bb623811fa3e5')
        croitie = Teams.objects.get(id='04acbb0416a54530b66eebca20ec1dc6')
        Games.objects.create(date=datetime.datetime.now(), is_finished=False, stadium="Bernabeo", home_team=maroc, away_team=france, goal_home_team=None, goal_away_team=None)
        Games.objects.create(date=datetime.datetime.now(), is_finished=False, stadium="Maracana", home_team=argentine, away_team=croitie, goal_home_team=None, goal_away_team=None)