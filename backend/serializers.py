#!/usr/bin/env python3

from backend.models import StudentUser
from django.contrib.auth.models import Group
from rest_framework import serializers


class StudentUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentUser
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
