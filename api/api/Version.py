from api.models import Version
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import VersionSerializer


class VersionViewSet(viewsets.ModelViewSet):
    serializer_class = VersionSerializer
    queryset = Version.objects.all()