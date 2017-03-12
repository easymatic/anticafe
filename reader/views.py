from django.http import HttpResponse
from rest_framework.decorators import api_view
from channels import Group


@api_view(['GET'])
def read(request, card):
    Group("chat").send({"text": card,})
    return HttpResponse(status=201)
