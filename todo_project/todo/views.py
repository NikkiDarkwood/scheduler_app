from django.shortcuts import redirect, render

from .models import TodoItem


def index(request):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    tasks_by_day = {}
    for day in days:
        tasks_by_day[day] = TodoItem.objects.filter(day=day)
    return render(request, "todo/index.html", {"tasks_by_day": tasks_by_day})


def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        day = request.POST.get("day")
        TodoItem.objects.create(title=title, day=day)
        return redirect("index")


def remove_todo(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.delete()
    return redirect("index")


def toggle_completed(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("index")
