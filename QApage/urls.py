from django.urls import path
from . import views

urlpatterns = [
    path("", views.QA, name="search_text")
]