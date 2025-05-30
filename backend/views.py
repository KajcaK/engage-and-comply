#!/usr/bin/env python3

from django.contrib.auth.models import Group
from backend.models import StudentUser, Document
from rest_framework import permissions, viewsets

from backend.serializers import (
    GroupSerializer, DocumentSerializer, StudentUserSerializer
)


class StudentUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = StudentUser.objects.all().order_by('-date_joined')
    serializer_class = StudentUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Document.objects.all().order_by('title')
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
