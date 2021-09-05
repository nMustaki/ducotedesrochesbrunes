import time
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.db import IntegrityError
from django.views.generic.base import TemplateView
from django.shortcuts import render
from registrator.models import TimeSlot, Visitor
from registrator.service_send_mail import my_send_mail


class IndexView(TemplateView):
    template_name = "registrator/index.html"


class SubscribeView(TemplateView):
    template_name = "registrator/subscribe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["times_5"] = []
        context["times_6"] = []
        for slot in TimeSlot.objects.all().order_by("time"):
            context[f"times_{slot.time.day}"].append(slot)

        context["show_details"] = False
        return context

    def get(self, request, *args, **kwargs):
        if not settings.SUBSCRIBE_ENABLED:
            return redirect("index")
        return super().get(request, args, kwargs)


def register(request, time_id):
    if not settings.SUBSCRIBE_ENABLED:
        return redirect("index")

    # try:
    time = get_object_or_404(TimeSlot.objects.select_for_update(), pk=time_id)
    try:
        nb_seats = int(request.POST.get("nb_seats"))
    except TypeError:
        print("Invalid number")
        return redirect("index")

    email = request.POST.get("email").lower().strip()
    name = request.POST.get("name")

    try:
        visitor = Visitor.objects.create(seats=nb_seats, time=time, name=name, email=email)
    except IntegrityError:
        existing_time = TimeSlot.objects.get(visitor__email=email)
        return render(request, "registrator/already_subscribed.html", {"time": existing_time})

    mail_sent = my_send_mail(visitor, time)

    return render(request, "registrator/subscribed.html", {"time": time, "mail_sent": mail_sent})
    # except Exception:
    #     return render(request, "registrator/error.html")


def unsubscribe(request):
    # Poor man's ddos protection
    time.sleep(1)
    try:
        email = request.POST.get("email", "").lower().strip()
        visitor = Visitor.objects.get(email__iexact=email)
        context = {"time": visitor.time}
        visitor.delete()
    except Visitor.DoesNotExist:
        context = {"time": None, "invalid_email": email}

    return render(request, "registrator/unsubscribed.html", context)


class DetailsView(SubscribeView):
    template_name = "registrator/subscribe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["show_details"] = True
        return context

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("admin/login/?next=/details")

        return super().get(request, args, kwargs)


class PicturesView(TemplateView):
    template_name = "registrator/pictures.html"


class ContactView(TemplateView):
    template_name = "registrator/contact.html"
