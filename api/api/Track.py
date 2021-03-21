from api.models import Track
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import TrackSerializer


class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()