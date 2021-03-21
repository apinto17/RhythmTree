
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()