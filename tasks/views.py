from django.shortcuts import render
from datetime import datetime


def task_list(request):
    tasks = ['Task 1', 'Task 2', 'Task 3']  # список задач
    current_date = datetime.now()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'current_date': current_date})

def task_detail(request, task_id):
    task = f'Task {task_id}'  # получение задачи из базы данных 
    return render(request, 'tasks/task_detail.html', {'task': task})
