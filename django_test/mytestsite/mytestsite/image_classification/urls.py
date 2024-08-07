from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("myfirst/", views.myfirst, name="first"),
    path("classification/", views.classification, name="classification"),
]
