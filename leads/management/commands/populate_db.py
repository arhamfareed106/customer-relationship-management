from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from leads.models import Lead, Agent, UserProfile, Category
from faker import Faker
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username="admin").exists():
            superuser = User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123"
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))

            # Create UserProfile for superuser
            UserProfile.objects.create(
                user=superuser
            )

        # Get or create the organizer's user profile
        organizer_profile = UserProfile.objects.first()
        if not organizer_profile:
            self.stdout.write(self.style.ERROR('No UserProfile found. Please create one first.'))
            return

        # Create some agents
        agent_users = []
        for i in range(5):
            username = f"agent{i+1}"
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=f"agent{i+1}@example.com",
                    password="agent123"
                )
                agent = Agent.objects.create(
                    user=user,
                    organisation=organizer_profile
                )
                agent_users.append(agent)
                self.stdout.write(self.style.SUCCESS(f'Agent {username} created successfully'))

        # If no agents were created, get existing ones
        if not agent_users:
            agent_users = list(Agent.objects.all())

        if not agent_users:
            self.stdout.write(self.style.ERROR('No agents available. Please create at least one agent first.'))
            return

        # Create categories
        categories = [
            "New Lead",
            "Contacted",
            "In Progress",
            "Qualified",
            "Unqualified",
            "Closed Won",
            "Closed Lost"
        ]

        created_categories = []
        for category_name in categories:
            category, created = Category.objects.get_or_create(
                name=category_name,
                organisation=organizer_profile
            )
            created_categories.append(category)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Category {category_name} created successfully'))

        # Create leads
        for _ in range(50):
            lead = Lead.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(25, 65),
                email=fake.email(),
                phone_number=fake.phone_number(),
                description=fake.text(max_nb_chars=200),
                agent=random.choice(agent_users),
                category=random.choice(created_categories),
                organisation=organizer_profile
            )
            self.stdout.write(self.style.SUCCESS(f'Lead {lead.first_name} {lead.last_name} created successfully'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
