from rest_framework import serializers
from Teams.models import Teams

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams 
        fields = ['id', 'name', 'group', 'is_eliminated']
