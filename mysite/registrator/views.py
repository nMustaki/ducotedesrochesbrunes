import random
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.db import transaction
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from registrator.flower_names import flower_names
from registrator.models import TimeSlot, Visitor


class IndexView(TemplateView):
    template_name = "registrator/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["times"] = TimeSlot.objects.all().order_by("time")
        context["show_details"] = False
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)


class SubscribeView(TemplateView):
    template_name = "registrator/subscribe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["times"] = TimeSlot.objects.all().order_by("time")
        context["show_details"] = False
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)


def register(request, time_id):
    try:
        with transaction.atomic():
            time = get_object_or_404(TimeSlot.objects.select_for_update(), pk=time_id)
            try:
                nb_seats = int(request.POST.get("nb_seats"))
            except TypeError:
                print("Invalid number")
                return redirect("index")

            email = request.POST.get("email")
            name = request.POST.get("name")

            visitor = Visitor.objects.create(seats=nb_seats, time=time, name=name, email=email)

            context = {"time": time, "flower": random.choice(list(flower_names))}
            return render(request, "registrator/subscribed.html", context)
    except Exception:
        return redirect("index")


class DetailsView(TemplateView):
    template_name = "registrator/subscribe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["times"] = TimeSlot.objects.all().order_by("time")
        context["show_details"] = True
        return context

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("admin/login/?next=/details")

        return super().get(request, args, kwargs)
