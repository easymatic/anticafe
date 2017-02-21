"""anticafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse
from rest_framework import routers

from person.views import PersonViewSet, CardViewSet
from session.views import SessionViewSet


def index(request):
    return HttpResponse("Welcome to AntiCafe")


router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'card', CardViewSet)
router.register(r'session', SessionViewSet)
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/', include(router.urls)),
    #  url(r'^person/', include('person.urls')),
    url(r'^session/', include('session.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
