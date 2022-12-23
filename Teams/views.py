from rest_framework import viewsets
from Teams.serializers import TeamSerializer
from Teams.models import Teams
from rest_framework.response import Response
from Teams.serializers import TeamSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects
    serializer_class = TeamSerializer
    
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset().order_by('name'), many=True)
        
        if request.query_params.get('name'):
            name_p = request.query_params.get('name')
            serializer = self.get_serializer(self.get_queryset().filter(name=name_p), many=True)
            
        if request.query_params.get('group'):
            group_p = request.query_params.get('group')
            serializer = self.get_serializer(self.get_queryset().filter(group=group_p), many=True)
            
        if request.query_params.get('is_eliminated'):
            is_eliminated_p = request.query_params.get('is_eliminated')
            serializer = self.get_serializer(self.get_queryset().filter(is_eliminated=is_eliminated_p), many=True)
            
        if request.query_params.get('name'):
            name_s = request.query_params.get('name')
            serializer = self.get_serializer(self.get_queryset().filter(name__startswith=name_s), many=True)
                      
        return Response(serializer.data)

        #initial
        # serializer = self.get_serializer(self.get_queryset(), many=True)
        # return Response(serializer.data)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
#second way to list (using filters that django provides)
# class TeamViewset2(viewsets.ModelViewSet):
#     queryset = Teams.objects
#     serializer_class = TeamSerializer
#     filterset_fields = ['name','group','is_eliminated']
#     search_fields = ['name']
    
