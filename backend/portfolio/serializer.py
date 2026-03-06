from rest_framework import serializers
from .models import Project, Experience, Service, PriseDeContact, SocialNetwork, Location


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "user",
            "resume",
            "title",
            "image",
            "link",
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "user",
            "start_date",
            "end_date",
            "role",
            "company_name",
            "description",
            "contract_type",
        ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "user",
            "name",
            "details",
            "service_type",
            "tools",
        ]


class PriseDeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriseDeContact
        fields = [
            "id",
            "user",
            "full_name",
            "object",
            "email",
            "message",
            "creation_date",
        ]
        read_only_fields = ["creation_date"]


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = [
            "id",
            "user",
            "platform_name",
            "link",
        ]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "id",
            "user",
            "city",
            "country",
            "longitude",
            "latitude",
        ]