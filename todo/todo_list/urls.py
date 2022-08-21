from django.urls import URLPattern, path 
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomUserLogin, RegisterPage

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomUserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('details/<int:pk>/', TaskDetail.as_view(), name='details'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete')

]
