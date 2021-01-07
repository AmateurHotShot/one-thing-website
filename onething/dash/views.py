from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Task
from .forms import TaskForm #CompletedTheTask

def index(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = User.objects.get(username=request.user)
            task.save()
            return redirect('/dash/')
        else:
            form = TaskForm()
    context = {'task_form': form}

    return render(request, "dash/index.html", context)

def dashboard_page(request):

    if request.user.is_authenticated:
        current_user = request.user
        user = User.objects.get(username=current_user)
        current_task = Task.objects.filter(user=user).filter(status=Task.IN_PROGRESS).latest('date_created')
        task_id = current_task.pk
        if request.method == 'POST':
            success_form = CompletedTheTask(request.POST)
            # Check that the form data is valid (use another form)
            # check that the user owns that particular task
            # get the task
            # set the status to complete
            # save the task
            # redirect the user back to the index

        task = {
        'my_task': current_task,
        'user_dude': current_user,
        'task_id': task_id,
        }
        return render(request, "dash/dashboard.html", task)
    else:
        return redirect('/login/')
    return


def success_page(request):
    current_task = Task.objects.get(id=1)
    task = {
        'object': current_task
    }
    return render(request, "dash/success.html", task)

def login_page(request):
    return render(request, 'dash/login.html')