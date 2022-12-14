from django.core.management.base import BaseCommand, CommandError
from Teams.models import Teams

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        help = 'Prepare the database for the project'
        self.verify()
        self.load_teams()

        
        
       
    def verify(self):
        count = Teams.objects.count()
        if(count == 0 ):
            self.load_teams()
        else:
            print(str(count)+" Objects  exits in database")   
        
    def load_teams(self):
        Teams.objects.all().delete()
        Teams.objects.create(name='Maroc',group='H',is_eliminated = False)
        Teams.objects.create(name='France',group='A',is_eliminated = False)
        Teams.objects.create(name='Argentine',group='C',is_eliminated = False) 
        Teams.objects.create(name='Croitie',group='D',is_eliminated = False)
        
         
        

        
        
        
        