from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("inscription", views.SubscribeView.as_view(), name="inscription"),
    path("details", views.DetailsView.as_view(), name="details"),
    path("register/<int:time_id>", views.register, name="register"),
]
