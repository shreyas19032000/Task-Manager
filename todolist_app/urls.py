from django.urls import path
from todolist_app import views


urlpatterns = [
    path('', views.todolist , name='todolist'),
    path('delete/<task_id>', views.task_delete , name='task_delete'),
    path('edit/<task_id>', views.task_edit , name='task_edit'),
    path('complete/<task_id>', views.task_complete , name='task_complete'),
    path('pending/<task_id>', views.task_pending , name='task_pending'),




    
    
]
