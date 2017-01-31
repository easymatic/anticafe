from rest_framework import viewsets
from .models import Person, Card
from .serializers import PersonSerializer, CardSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_fields = ('first_name', 'second_name',)


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_fields = ('indentifier',)
