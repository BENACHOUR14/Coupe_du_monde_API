from rest_framework import viewsets
from Games.serializers import GamesSerializer
from Games.models import Games
from rest_framework.response import Response

class GameViewSet(viewsets.ModelViewSet):
    queryset = Games.objects
    serializer_class = GamesSerializer
    
    def list(self, request):
        kw = request.query_params.get('kw')
        value = request.query_params.get('value')
        parametres_possible = ["date", "is_finished", "stadium","home_team","away_team"]
        arg = {}
        if kw and value:
            kws = kw.split("|")
            values = value.split("|")
            for i in range(len(kws)):
                if kws[i] in parametres_possible:
                    arg[kws[i]] = values[i]
        if arg:        
            serializer = self.get_serializer(self.get_queryset().filter(**arg), many=True)
        else:
            serializer = self.get_serializer(self.get_queryset(), many=True)
        
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
