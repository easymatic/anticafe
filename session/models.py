from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from person.models import Card


class Session(models.Model):
    start = models.DateTimeField(default=timezone.now, blank=True)
    end = models.DateTimeField(null=True)
    card = models.ForeignKey(Card)

    @property
    def duration(self):
        now = timezone.now()
        return (now-self.start).seconds

    @property
    def is_active(self):
        return not bool(self.end)

    def __str__(self):
        return "{}: {}".format(self.card, self.start)
