from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema
from .models import Project, Experience, Service, PriseDeContact, SocialNetwork, Location
from .serializer import (
    ProjectSerializer,
    ExperienceSerializer,
    ServiceSerializer,
    PriseDeContactSerializer,
    SocialNetworkSerializer,
    LocationSerializer,
)


# Project Views
@extend_schema(tags=['Projects'])
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Projects'])
class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Projects'])
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


# Experience Views
@extend_schema(tags=['Experiences'])
class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Experiences'])
class ExperienceCreateView(generics.CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Experiences'])
class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


# Service Views
@extend_schema(tags=['Services'])
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Services'])
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Services'])
class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


# Contact Views
@extend_schema(tags=['Contacts'])
class PriseDeContactListView(generics.ListAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Contacts'])
class PriseDeContactCreateView(generics.CreateAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Contacts'])
class PriseDeContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]


# SocialNetwork Views
@extend_schema(tags=['Social Networks'])
class SocialNetworkListView(generics.ListAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Social Networks'])
class SocialNetworkCreateView(generics.CreateAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Social Networks'])
class SocialNetworkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    permission_classes = [permissions.AllowAny]


# Location Views
@extend_schema(tags=['Locations'])
class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Locations'])
class LocationCreateView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Locations'])
class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]

