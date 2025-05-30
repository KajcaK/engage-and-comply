#!/usr/bin/env python3

from django.core.management.base import BaseCommand, CommandError
from backend.models import StudentUser, Document  # Replace with your actual model
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding the database...'))

        # 1. Seed StudentUsers
        StudentUser.objects.create(username='John Doe', email='john@doe.com', password='password')
        StudentUser.objects.create(username='Jane Doe', email='jane@doe.com', password='password')
        StudentUser.objects.create(username='Jean Doe', email='jean@doe.com', password='password')
        self.stdout.write(self.style.SUCCESS('Seeded StudentUsers...'))

        # 2. Seed Documents
        Document.objects.create(
            title="PACT Methodology V3: Methodology for Calculating and Exchanging Cradle-to-Gate Product Carbon Footprints (PCFs)",
            publish_date="2025-06-15", pdf_file="stub")
        Document.objects.create(
            title="GHG Protocol Standards (Corporate / Scope 3 / Product)",
            publish_date="2023-03-18", pdf_file="stub")
        self.stdout.write(self.style.SUCCESS('Seeded Documents...'))

        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'password')
            self.stdout.write(self.style.SUCCESS('Created superuser admin/password'))

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
