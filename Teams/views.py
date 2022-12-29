from rest_framework import viewsets
from Teams.serializers import TeamSerializer
from Teams.models import Teams
from rest_framework.response import Response
from Teams.serializers import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects
    serializer_class = TeamSerializer
        
    def list(self, request):
        qs = self.get_queryset()
        if request.query_params.get('name'):
            qs = qs.filter(name=request.query_params.get('name'))          
        if request.query_params.get('group'):
            qs = qs.filter(group=request.query_params.get('group'))
        if request.query_params.get('is_eliminated'):
            qs = qs.filter(is_eliminated=request.query_params.get('is_eliminated'))           
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
