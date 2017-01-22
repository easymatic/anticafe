from django.shortcuts import render
from rest_framework import viewsets
from .models import Person, Card, Session
from .serializers import PersonSerializer, CardSerializer, SessionSerializer

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello to anticafe")


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer



class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
