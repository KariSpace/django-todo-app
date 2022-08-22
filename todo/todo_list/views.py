# from attr import field
from multiprocessing import context
from re import template
from trace import Trace
from turtle import title
from jinja2 import Undefined 

# from django.http import HttpResponse


from django.shortcuts import render, redirect
from django.shortcuts import resolve_url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login

from django.http import HttpResponseRedirect
from .models import Task


class CustomUserLogin(LoginView):
   template_name = 'todo_list/login.html'
   fields = '__all__'
   redirect_authenticated_user = True

   def get_success_url(self,  **kwargs):
      context = super().get_context_data(**kwargs)
      print(context)
      if (context['next'] and context['next'] != '/'):
         return resolve_url(context['next'])
         
         # Old, bad way to redirect
         redirect_field_name = context['next'].split('/')
         return reverse_lazy(redirect_field_name[1], kwargs={'pk': redirect_field_name[2]})

      return reverse_lazy('tasks')




# Create your views here.
class TaskList(LoginRequiredMixin, ListView): 
   
   model = Task
   context_object_name = 'tasks'

   def get_context_data(self, **kwargs):

      context = super().get_context_data(**kwargs)
      print(context)
      context['tasks'] = context['tasks'].filter(user=self.request.user)
      context['count'] = context['tasks'].filter(complete=False).count()
      context['count_complete'] = context['tasks'].filter(complete=True).count()

      search_input = self.request.GET.get('search') or ''
      context['tasks'] = context['tasks'].filter(title__icontains=search_input)
      context['search_input'] = search_input
      return context



class RegisterPage(FormView):
   template_name = 'todo_list/register.html'
   form_class = UserCreationForm
   redirect_authenticated_user = True
   success_url = reverse_lazy('tasks')
   def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

   def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskDetail(LoginRequiredMixin, DetailView): 
   model = Task
   context_object_name = 'detail'
   template_name = 'todo_list/detail.html'

class TaskCreate(LoginRequiredMixin, CreateView): 
   model = Task

   # will make it more pretty sometime later
   fields =  ['title', 'description', 'complete', 'description', 'categories', 'have_deadline', 'deadline', 'importancy']
   success_url = reverse_lazy('tasks')

   def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         return context

   def form_valid (self, form) : 
      form.instance.user = self.request.user
      return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView): 
   model = Task
   
   # will make it more pretty sometime later
   fields = ['title', 'description', 'complete', 'description', 'categories', 'have_deadline', 'deadline', 'importancy']
   success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView): 
   model = Task
   context_object_name = 'task'
   success_url = reverse_lazy('tasks')
