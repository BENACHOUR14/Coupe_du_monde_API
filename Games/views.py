from rest_framework import viewsets
from Games.serializers import GamesSerializer
from Games.models import Games
from rest_framework.response import Response

class GameViewSet(viewsets.ModelViewSet):
    queryset = Games.objects
    serializer_class = GamesSerializer
            
    def list(self, request):
        qs = self.get_queryset()
        if request.query_params.get('date'):
            qs = qs.filter(date=request.query_params.get('date'))          
        if request.query_params.get('is_finished'):
            qs = qs.filter(is_finished=request.query_params.get('is_finished'))
        if request.query_params.get('stadium'):
            qs = qs.filter(stadium=request.query_params.get('stadium'))
        if request.query_params.get('home_team'):
            qs = qs.filter(home_team=request.query_params.get('home_team'))  
        if request.query_params.get('away_team'):
            qs = qs.filter(away_team=request.query_params.get('away_team'))             
        if request.query_params.get('search'):
            qs = qs.filter(name__contains=request.query_params.get('search'))
        return Response(self.get_serializer(qs, many=True).data)
        
    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
