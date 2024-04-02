from rest_framework import viewsets
from book_app.api import serializers
from book_app import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()
