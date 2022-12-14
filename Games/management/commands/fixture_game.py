from django.core.management.base import BaseCommand
from Games.models import Games
from Teams.models import Teams
import datetime

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.help = 'Insert two games as fixtures'
        self.load_Games()
                   
    def load_Games(self):
        try:
            Games.objects.all().delete()
            maroc = Teams.objects.get(name='Maroc')
            france = Teams.objects.get(name='France')
            argentine = Teams.objects.get(name='Argentine')
            croatie = Teams.objects.get(name='Croatie')
            Games.objects.create(date=datetime.datetime.now(), stadium="Bernabeo", home_team=maroc, away_team=france)
            Games.objects.create(date=datetime.datetime.now(), stadium="Maracana", home_team=argentine, away_team=croatie)
        except Teams.DoesNotExist:
            print("Please Add Teams First")
