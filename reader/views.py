from django.http import HttpResponse
from channels import Group


# Create your views here.
def read(request, card):
    Group("chat").send({"text": card,})
    return HttpResponse(status=201)
