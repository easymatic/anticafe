from __future__ import unicode_literals

from django.db import models


class Card(models.Model):
    indentifier = models.TextField()


class Person(models.Model):
    first_name = models.TextField(null=True)
    second_name = models.TextField(null=True)
    card = models.ForeignKey(Card)


class Session(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)
    card = models.ForeignKey(Card)
