from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("start", views.start, name="start"),
    path("breath", views.breath, name="breath"),
    path("final", views.final, name="final")
]
