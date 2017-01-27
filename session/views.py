from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from .models import Session
from person.models import Card
from person.serializers import CardSerializer
from .serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


@api_view(['POST'])
def start(request):
    serializer = SessionSerializer(data=request.data)
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
    session = card.session_set.first()
    if not session:
        return Response(
            "no session for this card", status=status.HTTP_404_NOT_FOUND)
    session.end = timezone.now()
    session.save()
    return Response(SessionSerializer(session).data)
