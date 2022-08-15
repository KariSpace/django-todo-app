# from attr import field
from trace import Trace
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import resolve
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# class CustomUserLogOut(LogoutView):
#    # template_name = 'todo_list/login.html'
#    fields = '__all__'
#    redirect_authenticated_user = True
#    success_url = reverse_lazy('login')

#    def get_success_url(self):
#        return reverse_lazy('login')


class CustomUserLogin(LoginView):
   template_name = 'todo_list/login.html'
   fields = '__all__'
   redirect_authenticated_user = True

   def get_success_url(self,  **kwargs):
      context = super().get_context_data(**kwargs)
      print(context)
      if (context['next']):
         redirect_field_name = context['next'].split('/')
         return reverse_lazy(redirect_field_name[1], kwargs={'pk': redirect_field_name[2]})

      return reverse_lazy('tasks')

# Create your views here.
class TaskList(LoginRequiredMixin, ListView): 
   
   model = Task
   context_object_name = 'tasks'



class TaskDetail(LoginRequiredMixin, DetailView): 
   model = Task
   context_object_name = 'detail'
   template_name = 'todo_list/detail.html'

class TaskCreate(LoginRequiredMixin, CreateView): 
   model = Task
   fields = '__all__'
   success_url = reverse_lazy('tasks')

class TaskUpdate(LoginRequiredMixin, UpdateView): 
   model = Task
   fields = '__all__'
   success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView): 
   model = Task
   context_object_name = 'task'
   success_url = reverse_lazy('tasks')
