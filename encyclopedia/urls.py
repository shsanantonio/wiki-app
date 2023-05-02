from django.urls import path
from . import views

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("add_page", views.add, name="add_page"),
    path("wiki/<str:title>/edit_page", views.edit, name="edit_page"),
    path("random_page", views.random_page, name="random_page"),
    path("search_page", views.search_page, name="search_page")
]
