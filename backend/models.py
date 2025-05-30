#!/usr/bin/env python3

from django.contrib.auth.models import AbstractUser
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    pdf_file = models.CharField(max_length=200)  # Link to google drive

    def __str__(self):
        return self.title

class StudentUser(AbstractUser):
    documents = models.ManyToManyField(
        'backend.Document', related_name='users'
    )

    def __str__(self):
        return self.username
