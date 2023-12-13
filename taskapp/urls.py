# urls.py
from django.urls import path
from .views import task_list,add_task,sum_of_even_numbers,ManageTask

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', add_task, name='add_task'),
    path('add_num', sum_of_even_numbers),
    path('tasks/manage_task', ManageTask.as_view(), name='manage_task'),

    # Add other URLs for forms, API, etc.
]
