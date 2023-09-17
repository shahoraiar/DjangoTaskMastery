from django.shortcuts import render , redirect
from task_app.models import TaskModel
from task_app.forms import TaskForm
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
# Create your views here.
class task_form(CreateView):
    model = TaskModel
    template_name = 'task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_task')

    def form_valid(self, form):
        # Set the user field to the currently logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)
    
def task_show(request):
    if request.user.is_authenticated:
        tasks = TaskModel.objects.filter(user=request.user).order_by('-priority')
    else:
        tasks = []

    return render(request, 'show_task.html', {'tasks': tasks})


class delete_task(DeleteView) : 
    model = TaskModel
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('show_task')

class edit_task(UpdateView) : 
    model = TaskModel
    template_name = 'edit_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_task')
    
def mark_completed(request , id) :
    task = TaskModel.objects.get(id = id)
    task.is_completed = True
    task.save()
    return redirect('completed')
    
def completed(request) : 
    task = TaskModel.objects.all()
    return render(request ,'completed.html' , {'completed_tasks':task})

def sort_tasks(request, sort_option):
    if request.user.is_authenticated:
        tasks = TaskModel.objects.filter(user=request.user)

        if sort_option == 'due_date':
            tasks = tasks.order_by('due_date')
        elif sort_option == 'priority':
            tasks = tasks.order_by('-priority')
        elif sort_option == 'category':
            tasks = tasks.order_by('category')
        elif sort_option == 'priority_level':
            tasks = tasks.order_by('priority')
        else:
            tasks = tasks.order_by('-priority')

        return render(request, 'show_task.html', {'tasks': tasks})
    