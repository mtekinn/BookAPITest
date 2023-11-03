from rest_framework import generics

from .serializers import BookSerializer
from .models import Book
from .tasks import add_book_to_library

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        add_book_to_library.delay(instance.title)