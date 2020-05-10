from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("blogpost/<str:title>", views.blogpost, name="blogpost"),

    # path("<str:country>/countryblogpost/<int:id>", views.countryblogpost, name="countryblogpost"),

    path("health/", views.health, name="health"),
    path("corona/", views.corona, name="corona"),
    path("india/", views.india, name="india"),
    path("usa/", views.usa, name="usa"),
    path("business/", views.business, name="business"),
    path("entertainment/", views.entertainment, name="entertainment"),
    path("general/", views.general, name="general"),
    path("science/", views.science, name="science"),
    path("sports/", views.sports, name="sports"),
    path("technology/", views.technology, name="technology"),


]
