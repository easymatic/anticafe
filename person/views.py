from django.shortcuts import render
from rest_framework import viewsets
from .models import Person, Card
from .serializers import PersonSerializer, CardSerializer

from django.http import HttpResponse


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
