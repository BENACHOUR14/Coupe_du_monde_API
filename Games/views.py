from rest_framework import viewsets
from Games.models import Games
from Games.serializers import GamesSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
