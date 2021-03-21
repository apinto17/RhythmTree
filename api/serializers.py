from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Project, Version, Track


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ["id"]

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        exclude = ["id", "project"]

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        exclude = ["id", "length"]