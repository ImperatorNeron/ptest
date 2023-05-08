from django.urls import path

from papp.views import index, second

urlpatterns = [
    path("", index, name="index"),
    path("second/", second, name="second"),
]