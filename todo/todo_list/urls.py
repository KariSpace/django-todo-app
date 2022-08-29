from django.urls import URLPattern, path , include
from .views import *
# TasksView, TaskListsView, CategoryView, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomUserLogin, RegisterPage

from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('login/', CustomUserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('categories/', CategoryView.as_view(), name='categories'),
    path('lists/', TaskListsView.as_view(), name='lists'),

    path('', TasksView.as_view(), name='tasks'),

    path('details/<int:pk>/', TaskDetail.as_view(), name='details'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('complete/<int:pk>/', TaskUpdate.as_view(), name='complete'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),

    # path('error', name='error')

]
