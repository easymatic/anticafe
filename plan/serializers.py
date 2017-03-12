from .models import Plan, Interval
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()


class PlanSerializer(BaseSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class IntervalSerializer(BaseSerializer):
    class Meta:
        model = Interval
        fields = ('start', 'end', 'cost', 'plan', 'duration')
