from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# View para listar e criar tarefas
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Task.objects.create(title=title)

        return redirect('task_list')

    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# View para concluir a tarefa
def task_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')


# View para excluir a tarefa
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
