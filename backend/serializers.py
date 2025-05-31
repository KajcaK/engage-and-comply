#!/usr/bin/env python3

from backend.models import StudentUser, Document
from django.contrib.auth.models import Group
from rest_framework import serializers


class StudentUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentUser
        fields = ['url', 'username', 'email', 'groups', 'documents']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['title', 'publish_date', 'pdf_file', 'users']
