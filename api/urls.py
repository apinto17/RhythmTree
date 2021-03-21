from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.api.Project import ProjectViewSet
from api.api.Track import TrackViewSet
from api.api.User import UserViewSet
from api.api.Version import VersionViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'track', TrackViewSet)
router.register(r'version', VersionViewSet)
router.register(r'user', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
