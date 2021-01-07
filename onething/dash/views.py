from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Task
from .forms import TaskForm

def index(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('/dash/')
        else:
            form = TaskForm()
    context = {'task_form': form}

    return render(request, "dash/index.html", context)

def dashboard_page(request):
    # if logged in
    # do a search on the task table where user = logged in user
    # filter the date create where user = logged in user
    # user.get username
    # django template logged in user
    if request.user.is_authenticated:
        current_user = request.user
        current_task = Task.objects.latest('date_created')
        task = {
        'my_task': current_task,
        'user_dude': current_user,
        }
        return render(request, "dash/dashboard.html", task)
    else:
        return login_page(request)


def success_page(request):
    current_task = Task.objects.get(id=1)
    task = {
        'object': current_task
    }
    return render(request, "dash/success.html", task)

def login_page(request):
    return render(request, 'dash/login.html')