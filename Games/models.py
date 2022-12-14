from django.db import models
from Teams.models import Teams
import uuid

# Create your models here.

class Games(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    is_finished = models.BooleanField(default=False, null=False, blank=False)
    stadium = models.CharField(max_length=80, null=False, blank=False)
    home_team = models.ForeignKey(Teams,on_delete=models.PROTECT, null=False, blank=False, related_name='home_team')
    away_team = models.ForeignKey(Teams,on_delete=models.PROTECT, null=False, blank=False, related_name='away_team')
    goal_home_team  = models.PositiveSmallIntegerField(null=True, blank=False)
    goal_away_team = models.PositiveSmallIntegerField(null=True, blank=False)   
       

