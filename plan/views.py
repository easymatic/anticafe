from rest_framework import viewsets
from .models import Plan, Interval
from .serializers import PlanSerializer, IntervalSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filter_fields = ('name', 'default_cost',)


class IntervalViewSet(viewsets.ModelViewSet):
    queryset = Interval.objects.all()
    serializer_class = IntervalSerializer
    filter_fields = ('start', 'end', 'cost', 'plan',)
