from django.urls import URLPattern, path , include
from .views import *
# TasksView, TaskListsView, CategoryView, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomUserLogin, RegisterPage

from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('login/', CustomUserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('categories/', CategoryView.as_view(), name='categories'),
    path('createCategory/', CategoryCreate.as_view(), name='createCategory'),
    path('updateCategory/<int:pk>/', CategoryUpdate.as_view(), name='updateCategory'),
    path('deleteCategory/<int:pk>/', CategoryDelete.as_view(), name='deleteCategory'),


    path('', TaskListsView.as_view(), name='lists'),
    path('createList/', TaskListsCreate.as_view(), name='createList'),
    path('updateList/<int:pk>/', TaskListsUpdate.as_view(), name='updateList'),
    path('deleteList/<int:pk>/', TaskListsDelete.as_view(), name='deleteList'),

    path('tasks/', TasksView.as_view(), name='tasks'),
    path('details/<int:pk>/', TaskDetail.as_view(), name='detailsTask'),
    path('createTask/', TaskCreate.as_view(), name='createTask'),
    path('updateTask/<int:pk>/', TaskUpdate.as_view(), name='updateTask'),
    path('completeTask/<int:pk>/', TaskUpdate.as_view(), name='completeTask'),
    path('deleteTask/<int:pk>/', TaskDelete.as_view(), name='deleteTask'),

    # path('error', name='error')

]
