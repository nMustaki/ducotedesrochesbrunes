from django.db import models
from django.db.models import Sum


class TimeSlot(models.Model):
    time = models.DateTimeField("date published", unique=True)
    max_seats = models.IntegerField(default=30)
    duration = models.DurationField()

    def get_remaining_seats(self):
        nb_visitors = self.visitor_set.all().aggregate(Sum("seats"))["seats__sum"] or 0
        return max(0, self.max_seats - nb_visitors)

    def end(self):
        return self.time + self.duration

    def get_available_seats(self):
        return range(1, self.get_remaining_seats() + 1)

    def get_used_names(self):
        return self.visitor_set.values_list("identifier", flat=True)


class Visitor(models.Model):
    time = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    seats = models.IntegerField(default=1)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    class Meta:
        unique_together = [("name", "time")]
        ordering = ["name"]
