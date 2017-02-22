from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^read/(?P<card>.*)$', views.read),
]
