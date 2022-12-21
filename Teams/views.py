from rest_framework import viewsets
from Teams.serializers import TeamSerializer
from Teams.models import Teams

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer
