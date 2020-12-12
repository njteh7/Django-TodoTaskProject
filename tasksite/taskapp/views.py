from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class TaskListView(ListView):
    model = Task
    template_name = 'myapp/index.html'
    context_object_name = 'task_list'
    task_list = Task.objects.all

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get('name', '')
            description = request.POST.get('description', '')
            priority = request.POST.get('priority', '')
            date = request.POST.get('date', '')
            task = Task(name=name, description=description, priority=priority, date=date)
            task.save()
            return redirect('/')

        return render(request, 'myapp/index.html', {'task_list':task_list})

class TaskDetailView(DetailView):
    model = Task
    template_name = 'myapp/detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'myapp/update.html'
    context_object_name = 'task'
    fields = ('name', 'description', 'priority', 'date')
    
    def get_success_url(self):
        return reverse_lazy('index')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'myapp/delete.html'
    success_url = reverse_lazy('index')

def delete(request, taskid):
    task = Task.objects.get(id=taskid)

    if "yes" in request.POST:
        task.delete()
        return redirect('/')
    elif "no" in request.POST:
        return redirect('/')
    return render(request, 'myapp/delete.html', {'task':task})
    