from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("details", views.index, name="details"),
    path("register/<int:time_id>", views.register, name="register"),
]
