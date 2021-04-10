from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.db import transaction
import random

from registrator.flower_names import flower_names
from registrator.models import Time, Visitor


def index(request):
    context = {"times": Time.objects.all().order_by("time")}
    return render(request, "registrator/index.html", context)


def register(request, time_id):
    with transaction.atomic():
        time = get_object_or_404(Time.objects.select_for_update(), pk=time_id)
        try:
            nb_seats = int(request.POST.get("nb_seats"))
        except TypeError:
            print("Invalid number")
            return redirect("index")

        if nb_seats <= time.get_remaining_seats():
            used = time.get_used_names()
            name = random.choice(list(flower_names))
            while name["name"] in used:
                name = random.choice(list(flower_names))

            visitor = Visitor.objects.create(seats=nb_seats, time=time, identifier=name["name"])

        return redirect("index")


def details(request):
    context = {"times": Time.objects.all().order_by("time"), "show_details": True}
    return render(request, "registrator/index.html", context)
