from django.urls import URLPattern, path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('details/<int:pk>/', TaskDetail.as_view(), name='details')
]
