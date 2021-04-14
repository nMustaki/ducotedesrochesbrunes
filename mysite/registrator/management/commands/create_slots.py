from datetime import timedelta
from django.core.management.base import BaseCommand, CommandError
from registrator.models import TimeSlot
from django.utils import timezone


class Command(BaseCommand):
    help = "Init db"

    def handle(self, *args, **options):
        duration = timedelta(hours=1, minutes=30)

        the_5 = timezone.localtime().replace(year=2021, month=6, day=5, hour=10, minute=0, second=0, microsecond=0)
        the_5_max = timezone.localtime().replace(year=2021, month=6, day=5, hour=18, minute=30, second=0, microsecond=0)

        while the_5 < the_5_max:
            slot = TimeSlot.objects.create(duration=duration, max_seats=15, time=the_5)
            print(slot.time)
            the_5 = the_5 + timedelta(minutes=30)

        the_6 = timezone.localtime().replace(year=2021, month=6, day=6, hour=10, minute=0, second=0, microsecond=0)
        the_6_max = timezone.localtime().replace(year=2021, month=6, day=6, hour=18, minute=30, second=0, microsecond=0)

        while the_6 < the_6_max:
            slot = TimeSlot.objects.create(duration=duration, max_seats=15, time=the_6)
            print(slot.time)
            the_6 = the_6 + timedelta(minutes=30)

        self.stdout.write(self.style.SUCCESS("Successfully"))
