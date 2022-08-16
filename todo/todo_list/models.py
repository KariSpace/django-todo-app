from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    categories = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    have_deadline = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    importancy = models.IntegerField(blank=True, default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])



    def __str__(self): 
        return self.title

    class Meta:
        ordering = ['complete', 'deadline', 'importancy']

