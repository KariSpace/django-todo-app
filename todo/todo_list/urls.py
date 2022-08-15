from django.urls import URLPattern, path 
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomUserLogin

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', CustomUserLogin.as_view(), name='login'),
    path('', TaskList.as_view(), name='tasks'),
    path('details/<int:pk>/', TaskDetail.as_view(), name='details'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete')

]
