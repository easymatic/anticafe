from .models import Card, Person
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()


class CardSerializer(BaseSerializer):
    class Meta:
        model = Card
        fields = ('id', 'indentifier')


class PersonSerializer(BaseSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'second_name', 'card')
