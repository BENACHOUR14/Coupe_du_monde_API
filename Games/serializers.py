from rest_framework import serializers
from Games.models import Games
from Teams.serializers import TeamSerializer

class GamesSerializer(serializers.ModelSerializer):
    home_team = TeamSerializer()
    away_team = TeamSerializer()
    class Meta:
        model = Games
        fields = ['id', 'date', 'is_finished', 'stadium', 'home_team', 'away_team', 'goal_home_team', 'goal_away_team']
