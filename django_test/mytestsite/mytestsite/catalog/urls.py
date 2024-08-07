from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("myfirst/", views.myfirst, name="myfirst"),
    path("classification/", views.classification, name="classification"),
    path("fileupload/", views.fileupload, name="fileupload"),
]
