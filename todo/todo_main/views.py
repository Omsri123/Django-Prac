from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updates_at')
    cp_tasks = Task.objects.filter(is_completed = True)
    print(cp_tasks)
    context = {
        'tasks' : tasks,
        'cpTasks' : cp_tasks,
    }
    return render(request, 'index.html', context)