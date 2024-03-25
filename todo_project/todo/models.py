from django.db import models


class TodoItem(models.Model):
    DAY_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    day = models.CharField(max_length=20, choices=DAY_CHOICES)

    def __str__(self):
        return self.title
