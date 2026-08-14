from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):

    queryset = Person.objects.all().order_by("-id")

    serializer_class = PersonSerializer

    parser_classes = [
        MultiPartParser,
        FormParser,
    ]