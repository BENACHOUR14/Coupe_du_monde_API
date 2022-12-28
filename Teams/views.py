from rest_framework import viewsets
from Teams.serializers import TeamSerializer
from Teams.models import Teams
from rest_framework.response import Response
from Teams.serializers import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects
    serializer_class = TeamSerializer
    
    def list(self, request):
        kw = request.query_params.get('kw')
        value = request.query_params.get('value')
        parametres_possible = ["name", "is_eliminated", "group"]
        arg = {}
        if kw and value:
            kws = kw.split(",")
            values = value.split(",")
            for i in range(len(kws)):
                if kws[i] in parametres_possible:
                    arg[kws[i]] = values[i]
        if arg:        
            serializer = self.get_serializer(self.get_queryset().filter(**arg), many=True)
        elif kw == "search":
            serializer = self.get_serializer(self.get_queryset().filter(name__startswith=value), many=True)      
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
