
from django.http import HttpResponse
from .models import project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django App!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'Richard'
    return render(request, 'about.html', {
        'username': username 
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)
 
def projects(request):
    # projects = list(project.objects.values())
    projects = project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    # task = Task.objects.get(tittle=tittle)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
        'form': CreateNewTask()
        })
    else:
        Task.objects.create(tittle=request.POST['tittle'], description=request.POST['description'], project_id=2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
    else:
        project.objects.create(name=request.POST["name"])
        return redirect(projects)

def project_detail(request, id):
    projects = get_object_or_404(project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'detail.html', {
        'project': projects,
        'tasks': tasks
    })