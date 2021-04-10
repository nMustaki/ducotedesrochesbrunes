from datetime import timedelta
from django.core.management.base import BaseCommand, CommandError
from registrator.models import TimeSlot
from django.utils import timezone


class Command(BaseCommand):
    help = "Init db"

    def handle(self, *args, **options):
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 5, 8))
        )
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 5, 9))
        )
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 5, 12))
        )
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 5, 13))
        )
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 5, 14))
        )
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 5, 15))
        )

        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 6, 8))
        )
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 6, 9))
        )
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 6, 12))
        )
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 6, 13))
        )
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 6, 14))
        )
        TimeSlot.objects.create(
            duration=timedelta(hours=1), max_seats=30, time=timezone.make_aware(timezone.datetime(2021, 6, 6, 15))
        )

        self.stdout.write(self.style.SUCCESS("Successfully"))
