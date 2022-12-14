from django.core.management.base import BaseCommand, CommandError
from Teams.models import Teams

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.help = 'Insert four teams as fixtures'
        self.load_teams()

    def load_teams(self):
        Teams.objects.all().delete()
        Teams.objects.create(name='Maroc', group='H', is_eliminated=False)
        Teams.objects.create(name='France', group='A', is_eliminated=False)
        Teams.objects.create(name='Argentine', group='C', is_eliminated=False) 
        Teams.objects.create(name='Croatie', group='D', is_eliminated=False)
