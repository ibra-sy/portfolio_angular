from django.db import models
from django.conf import settings

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="User", 
        related_name="projects",
        null=True,
        blank=True
    )
    resume = models.TextField(verbose_name="Project summary")
    title = models.CharField(max_length=50, verbose_name="Title")
    image = models.CharField(max_length=50, verbose_name="Image")
    link = models.CharField(max_length=50, verbose_name="Link")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Experience(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="experiences",
        null=True,
        blank=True,
    )
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")
    role = models.CharField(max_length=30, verbose_name="Role")
    company_name = models.CharField(max_length=30, verbose_name="Company name")
    description = models.TextField(verbose_name="Description")  # TextField au lieu de CharField
    contract_type = models.CharField(max_length=30, verbose_name="Contract type")
    
    def __str__(self):
        return f"{self.role} at {self.company_name}"
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

class Service(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="User", 
        related_name="services",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=30, verbose_name="Service name")
    details = models.TextField(verbose_name="Details")  
    service_type = models.CharField(max_length=30, verbose_name="Service type")
    tools = models.CharField(max_length=100, verbose_name="Tools") 
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class PriseDeContact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User", related_name="contacts_recus", null=True, blank=True)
    full_name = models.CharField(max_length=70, verbose_name="Full name")
    object = models.CharField(max_length=30, verbose_name="Object")
    email = models.EmailField(verbose_name="Email")  # EmailField au lieu de CharField
    message = models.TextField(verbose_name="Message")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    
    def __str__(self):
        return f"{self.full_name} - {self.subject}"
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class SocialNetwork(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="User", 
        related_name="social_networks",
        null=True,
        blank=True
    )
    platform_name = models.CharField(max_length=30, verbose_name="Platform name")
    link = models.URLField(verbose_name="Link")  # URLField au lieu de CharField
    
    def __str__(self):
        return self.platform_name
    
    class Meta:
        verbose_name = "Social network"
        verbose_name_plural = "Social networks"

class Location(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="User", 
        related_name="locations",
        null=True,
        blank=True
    )
    city = models.CharField(max_length=50, verbose_name="City")
    country = models.CharField(max_length=50, verbose_name="Country")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    
    def __str__(self):
        return f"{self.city}, {self.country}"
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"