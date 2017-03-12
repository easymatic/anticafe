from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import timedelta
from person.models import Card
from copy import deepcopy


class Session(models.Model):
    start = models.DateTimeField(default=timezone.now, blank=True)
    end = models.DateTimeField(null=True)
    card = models.ForeignKey(Card)
    cost_field = models.FloatField(null=True, default=None)

    @property
    def duration(self):
        now = self.end
        if not now:
            now = timezone.now()
        return (now-self.start)

    @property
    def is_active(self):
        return not bool(self.end)

    @property
    def cost(self):
        if self.cost_field:
            return self.cost_field
        plan = self.card.plan
        if not plan:
            return 0
        query = plan.interval_set
        query = query.filter(start__lte=self.duration)
        # TODO: need to find better solution
        query = query.order_by('start')
        intervals = []
        for i in query:
            intervals.append([i.start, i.end, i.cost])

        def c(delta, cost):
            return delta.total_seconds()/60*cost
        if not intervals:
            return c(self.duration, plan.default_cost)
        if self.duration < intervals[-1][1]:
            intervals[-1][1] = self.duration
        intervals = [(end-start, cost) for start, end, cost in intervals]
        diff = self.duration - sum(
            [delta for delta, _ in intervals], timedelta())
        all_cost = sum([c(delta, cost) for delta, cost in intervals])
        all_cost += c(diff, plan.default_cost)
        return all_cost

    def __str__(self):
        return "{}: {}".format(self.card, self.start)
