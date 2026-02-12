from django.urls import path
from django.views.generic import RedirectView
from .views import task_list, task_complete, task_delete

urlpatterns = [
    path('', RedirectView.as_view(url='/tasks/', permanent=False), name='index'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/<int:task_id>/complete/', task_complete, name='task_complete'),
    path('tasks/<int:task_id>/delete/', task_delete, name='task_delete'),
]