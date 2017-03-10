from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from datetime import timedelta
from .models import Session
from person.models import Card
from person.serializers import CardSerializer
from .serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    filter_fields = ('start', 'end', 'card')

    def get_queryset(self):
        if 'is_active' in self.request.query_params:
            return Session.objects.filter(end__isnull=True)
        return Session.objects.all()


@api_view(['POST'])
def calc(request):
    intervals = []

    def c(delta, cost):
        return delta.seconds/60*cost
    default_cost = 5  # per second
    duration = timedelta(minutes=28)
    if duration < intervals[-1][1]:
        intervals[-1][1] = duration
    intervals = [(end-start, cost) for start, end, cost in intervals]
    diff = duration - sum([delta for delta, _ in intervals], timedelta())
    all_cost = sum([c(delta, cost) for delta, cost in intervals])
    all_cost += c(diff, default_cost)


@api_view(['POST'])
def start(request):
    card_serializer = CardSerializer(data=request.data)
    if not card_serializer.is_valid():
        return Response(
            card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    indentifier = card_serializer.validated_data['indentifier']
    card = Card.objects.filter(indentifier=indentifier).first()
    if not card:
        return Response("No such card", status=status.HTTP_404_NOT_FOUND)
    open_sessions = Session.objects.filter(card=card.id, end=None)
    if open_sessions:
        return Response('Session for this card already opened',
                        status=status.HTTP_400_BAD_REQUEST)
    serializer = SessionSerializer(data={'card': card.id})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def stop(request):
    card_serializer = CardSerializer(data=request.data)
    if not card_serializer.is_valid():
        return Response(
            card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    indentifier = card_serializer.validated_data['indentifier']
    card = Card.objects.filter(indentifier=indentifier).first()
    if not card:
        return Response("No such card", status=status.HTTP_404_NOT_FOUND)
    session = card.session_set.filter(end=None).first()
    if not session:
        return Response(
            "no session for this card", status=status.HTTP_404_NOT_FOUND)
    if not session.is_active:
        return Response("Session not active",
                        status=status.HTTP_400_BAD_REQUEST)
    session.end = timezone.now()
    session.save()
    return Response(SessionSerializer(session).data)
