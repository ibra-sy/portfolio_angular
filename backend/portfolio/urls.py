"""
URL configuration for portfolioAngularBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectDetailView,
    ExperienceListView,
    ExperienceCreateView,
    ExperienceDetailView,
    ServiceListView,
    ServiceCreateView,
    ServiceDetailView,
    PriseDeContactListView,
    PriseDeContactCreateView,
    PriseDeContactDetailView,
    SocialNetworkListView,
    SocialNetworkCreateView,
    SocialNetworkDetailView,
    LocationListView,
    LocationCreateView,
    LocationDetailView,
)

urlpatterns = [
    # Project URLs
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    # Experience URLs
    path('experiences/', ExperienceListView.as_view(), name='experience-list'),
    path('experiences/create/', ExperienceCreateView.as_view(), name='experience-create'),
    path('experiences/<int:pk>/', ExperienceDetailView.as_view(), name='experience-detail'),

    # Service URLs
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),

    # Contact URLs
    path('contacts/', PriseDeContactListView.as_view(), name='contact-list'),
    path('contacts/create/', PriseDeContactCreateView.as_view(), name='contact-create'),
    path('contacts/<int:pk>/', PriseDeContactDetailView.as_view(), name='contact-detail'),

    # SocialNetwork URLs
    path('social-networks/', SocialNetworkListView.as_view(), name='socialnetwork-list'),
    path('social-networks/create/', SocialNetworkCreateView.as_view(), name='socialnetwork-create'),
    path('social-networks/<int:pk>/', SocialNetworkDetailView.as_view(), name='socialnetwork-detail'),

    # Location URLs
    path('locations/', LocationListView.as_view(), name='location-list'),
    path('locations/create/', LocationCreateView.as_view(), name='location-create'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
]
