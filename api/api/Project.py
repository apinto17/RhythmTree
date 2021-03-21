from api.models import Project
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()