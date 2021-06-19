from tasks.models import *
from rest_framework import viewsets, permissions
from .serializers import *

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = TaskSerializer

class TileViewSet(viewsets.ModelViewSet):
  queryset = Tile.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = TileSerializer