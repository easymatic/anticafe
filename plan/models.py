from __future__ import unicode_literals

from django.db import models


class Plan(models.Model):

    name = models.TextField()
    default_cost = models.FloatField()

    def __str__(self):
        return self.name


class Interval(models.Model):

    start = models.DurationField()
    end = models.DurationField()
    cost = models.FloatField()
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    @property
    def duration(self):
        return self.end - self.start

    def __str__(self):
        return "{}, {}-{} : {}".format(self.plan.name, self.start,
                                       self.end, self.cost)
