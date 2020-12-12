from django.db import models
import datetime

PRIORITY_CHOICES = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
)

# Create your models here.
class Task(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    date = models.DateField(default=datetime.date.today)