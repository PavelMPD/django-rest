from rest_framework import viewsets

from main import models
from main import serializers


class AgentViewSet(viewsets.ModelViewSet):
    queryset = models.Agent.objects.all().order_by('-user__date_joined')
    serializer_class = serializers.AgentSerializer
