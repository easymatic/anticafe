from .models import Session
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()


class SessionSerializer(BaseSerializer):
    class Meta:
        model = Session
        fields = ('id', 'start', 'end', 'card', 'duration', 'is_active')
