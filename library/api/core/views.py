from rest_framework import viewsets
from .serializers import LibrarySerializer
from .models import Library

class LibraryViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()