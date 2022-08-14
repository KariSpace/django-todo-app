from django.urls import URLPattern, path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('details/<int:pk>/', TaskDetail.as_view(), name='details'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete')

]
