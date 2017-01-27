from __future__ import unicode_literals

from django.db import models


class Card(models.Model):
    indentifier = models.TextField()

    def __str__(self):
        return self.indentifier


class Person(models.Model):
    first_name = models.TextField(null=True)
    second_name = models.TextField(null=True)
    card = models.ForeignKey(Card)

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name)
