from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.
class TasksList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_name = models.CharField(max_length=200)
        
    class Meta:
        ordering = ['task_name']

    def __str__(self):
        return self.task_name


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category_name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tasks_list = models.ForeignKey(TasksList, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category)
    description = models.TextField(null=True, blank=True)
    importancy = models.IntegerField(blank=True, default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    have_deadline = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self): 
        return self.title

    class Meta:
        ordering = ['-importancy', 'deadline']


