from django.urls import URLPattern, path
from .views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('details/<int:pk>/', TaskDetail.as_view(), name='details'),
    path('create/', TaskCreate.as_view(), name='create')
]
