from django.contrib.auth.models import User
from django.http import response
from django.http.response import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.urls import reverse


from .models import Task
from .forms import TaskForm

def index(request):
    form = TaskForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = User.objects.get(username=request.user)
                task.save()
                return redirect('/dash/')
            else:
                form = TaskForm()
        else:
            return redirect(reverse("login"))

    context = {'task_form': form}

    return render(request, "dash/index.html", context)

def dashboard_page(request):

    if request.user.is_authenticated:
        current_user = request.user
        user = User.objects.get(username=current_user)
        current_task = Task.objects.filter(user=user).filter(status=Task.IN_PROGRESS).latest('date_created')
        task_id = current_task.pk
        task = {
        'my_task': current_task,
        'task_id': task_id,
        'task_status': current_task.status,
        }

        if request.method == 'POST':
            if current_user == current_task.user:
                if 'done_button' in request.POST:
                        current_task.status = Task.SUCCESS
                        current_task.save()
                        print('POSTED AND SAVED, YALL')
                        return HttpResponseRedirect(reverse('success'))
                elif 'next_task' in request.POST:
                    current_task.status = Task.FAIL
                    current_task.save()
                    return redirect(reverse("index"))
            else:
                return Http404

            # Check that the form data is valid (use another form)
            # check that the user owns that particular task
            # get the task
            # set the status to complete
            # save the task
            # redirect the user back to the index
        return render(request, "dash/dashboard.html", task)
    #else:
    #    return redirect('/login/')
    return


def success_page(request):
    user = request.user
    completed_task = Task.objects.filter(user=user).filter(status=Task.SUCCESS).latest('date_created')
    task = {
        'completed_task': completed_task
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'next_task' in request.POST:
                return redirect(reverse("index"))
    return render(request, "dash/success.html", task)

def login_page(request):
    return render(request, 'dash/login.html')


def logout_page(request):
    return render(request, "<h1>Logout Page</h1>")

def signup_page(request):
    return render (request, '')