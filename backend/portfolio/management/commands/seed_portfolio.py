from datetime import date
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from portfolio.models import (
    Project,
    Experience,
    Service,
    PriseDeContact,
    SocialNetwork,
    Location,
)


class Command(BaseCommand):
    help = "Seed the database with initial portfolio data for SYLLA SCHEICKNA IBRAHIM"

    def handle(self, *args, **options):
        User = get_user_model()

        user, created = User.objects.get_or_create(
            username="ibra",
            defaults={
                "email": "hamahoullah.sylla@gmail.com",
                "first_name": "SYLLA",
                "last_name": "SCHEICKNA IBRAHIM",
                "description": (
                    "Student in Computer Science (Network & Telecommunications) | "
                    "Python Enthusiast | Future Network & Software Innovator | "
                    "Aspiring Cybersecurity Professional.\n\n"
                    "As a third-year Computer Science student at the Institut Ivoirien de Technologie, "
                    "I am driven by a strong passion for network engineering, software development, and "
                    "cybersecurity. I am constantly exploring how these fields connect to build secure, "
                    "scalable, and efficient digital systems.\n\n"
                    "With a solid foundation in Python, hands-on exposure to networking technologies, "
                    "and a deep curiosity for how systems operate behind the scenes, I am committed to "
                    "growing into a highly skilled professional capable of designing and maintaining "
                    "future-ready infrastructures.\n\n"
                    "I view technology not just as a field of study, but as a space for innovation, "
                    "problem-solving, and long-term impact. I am eager to collaborate on meaningful "
                    "projects, learn from experienced professionals, and contribute to solutions that "
                    "truly make a difference."
                ),
                "telephone": "0701633006",
                "lien_cv": "https://drive.google.com/file/d/1r5KLMkCD7nw8pkwmiYOpIM8rEAk1Is6x/view?usp=sharing",
            },
        )

        if created:
            # Set a simple default password; change it later via createsuperuser or admin.
            user.set_password("changeme123")
            user.save()

        self.stdout.write(self.style.SUCCESS(f"Using user: {user.username} (id={user.id})"))

        # Location
        Location.objects.all().delete()
        Location.objects.create(
            user=user,
            city="Grand-Bassam",
            country="Côte d'Ivoire",
            longitude=Decimal("-3.738300"),
            latitude=Decimal("5.209000"),
        )

        # Social networks
        SocialNetwork.objects.all().delete()
        SocialNetwork.objects.create(
            user=user,
            platform_name="GitHub",
            link="https://github.com/ibra-sy",
        )
        SocialNetwork.objects.create(
            user=user,
            platform_name="LinkedIn",
            link="https://www.linkedin.com/in/scheickna-ibrahim-sylla-50a916315?utm_source=share_via&utm_content=profile&utm_medium=member_android",
        )

        # Experiences
        Experience.objects.all().delete()
        Experience.objects.create(
            user=user,
            start_date=date(2025, 10, 1),
            end_date=date(2025, 12, 31),
            role="Mobile Applications Developer",
            company_name="ITALIA CONSTRUCTION",
            description=(
                "Development of a complete construction project tracking platform for Italia Construction "
                "(BTP sector). The solution includes a client mobile app for real-time project follow-up, "
                "an internal app for site teams, full workflow management, document sharing and an "
                "integrated online payment module."
            ),
            contract_type="Apprenticeship",
        )
        Experience.objects.create(
            user=user,
            start_date=date(2025, 7, 1),
            end_date=date(2025, 8, 31),
            role="Network Administration Intern",
            company_name="F2i Immobilier",
            description=(
                "Worked on managing and maintaining the internal network: configuration, incident "
                "diagnostics, basic security measures, user support and documentation of procedures "
                "for smoother IT operations in the real estate sector."
            ),
            contract_type="Internship",
        )

        # Services
        Service.objects.all().delete()
        Service.objects.create(
            user=user,
            name="Software & Network Development",
            details=(
                "Design and development of reliable digital solutions, from Python-based tools to "
                "network-aware applications, with a focus on scalability and security."
            ),
            service_type="Development",
            tools="Python, Django, REST APIs",
        )
        Service.objects.create(
            user=user,
            name="Responsive & Mobile-First Interfaces",
            details=(
                "Building user interfaces that adapt to all devices to ensure a smooth experience "
                "on desktop, tablet and mobile."
            ),
            service_type="Frontend",
            tools="Flutter, HTML, CSS",
        )
        Service.objects.create(
            user=user,
            name="Network & Infrastructure Basics",
            details=(
                "Support on small network setups, monitoring and troubleshooting connectivity issues, "
                "with attention to security good practices."
            ),
            service_type="Network",
            tools="GNS3, basic routing/switching tools",
        )

        # Projects
        Project.objects.all().delete()
        Project.objects.create(
            user=user,
            title="Construction Project Tracking Platform",
            resume=(
                "End-to-end mobile platform for Italia Construction, enabling clients and internal teams "
                "to follow construction projects in real time with tasks, progress, documents and payments."
            ),
            image="project_italia_construction.png",
            link="https://github.com/ibra-sy",  # replace with real repo when available
        )

        self.stdout.write(self.style.SUCCESS("Portfolio data successfully seeded."))

