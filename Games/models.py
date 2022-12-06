from django.db import models
import Teams
import uuid

# Create your models here.

class Games(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    isfinished = models.BooleanField(default=False,null=False,blank=False)
    stadium = models.CharField(max_length=80,null=False,blank=False)
    home_team = models.ForeignKey(Teams, null=False,blank=False)
    away_team = models.ForeignKey(Teams, null=False,blank=False)
    goal_home_team  = models.PositiveSmallIntegerField(null=False,blank=False)
    goal_away_team = models.PositiveSmallIntegerField(null=False,blank=False)      

