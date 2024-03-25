from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_todo, name="add_todo"),
    path("remove/<int:todo_id>/", views.remove_todo, name="remove_todo"),
    path("toggle/<int:todo_id>/", views.toggle_completed, name="toggle_completed"),
]
