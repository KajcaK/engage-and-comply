#!/usr/bin/env python3

from django.contrib.auth.models import Group
from backend.models import StudentUser, Document
import backend.llm
from rest_framework import permissions, viewsets
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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


@api_view(['GET'])  # Only allow GET requests
def generate_test_questions(request, document_id):
    #try:
    #    document = Document.objects.get(pk=document_id)
    #except Document.DoesNotExist:
    #    return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)

    #serializer = DocumentSerializer(document)  # Serialize the document data (optional)

    # Generate questions using your function
    questions = backend.llm.start_session("pact-methodology.pdf")

    return Response({"questions": questions}, status=status.HTTP_200_OK)
