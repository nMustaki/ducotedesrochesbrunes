from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("photos", views.PicturesView.as_view(), name="pictures"),
    path("inscription", views.SubscribeView.as_view(), name="inscription"),
    path("details", views.DetailsView.as_view(), name="details"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("register/<int:time_id>", views.register, name="register"),
    path("unsubscribe", views.unsubscribe, name="unsubscribe"),
]
