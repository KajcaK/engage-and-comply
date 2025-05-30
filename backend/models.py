#!/usr/bin/env python3

from django.contrib.auth.models import AbstractUser
from django.db import models
from io import BytesIO
import PyPDF2
import os

class Document(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    pdf_file = models.FileField(upload_to='pdfs/')
    pdf_text = models.TextField(default="")

    def __str__(self):
        return self.title

    def extract_text(self):
        """Extracts text from the PDF file."""
        text = ''
        try:
            file_path = self.pdf_file.path

            if os.path.exists(file_path):
                with open(file_path, 'rb') as pdf_file_obj:
                    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        text += page.extract_text()
            else:
                print(f"Error: PDF file not found at {file_path}")
                return "PDF Not Found"

        except Exception as e:
            print(f"Error extracting text: {e}")
            return f"Extraction Error: {e}"  # Provide extraction error message
        with open('doc_file.txt', 'w') as f:
            f.write(text)
        return text


    def save(self, *args, **kwargs):
        """Overrides the save method to extract text when a new PDF is uploaded."""
        if not self.pk and self.pdf_file:  # Only extract for new documents with a PDF
            try:
                self.pdf_text = self.extract_text() #set the text
            except Exception as e:
                print(f"Error during text extraction: {e}")

        super().save(*args, **kwargs) #Call "real" save()


class StudentUser(AbstractUser):
    documents = models.ManyToManyField(
        'backend.Document', related_name='users'
    )

    def __str__(self):
        return self.username
