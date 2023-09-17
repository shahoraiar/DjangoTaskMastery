from django import forms
from task_app.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription', 'due_date', 'priority', 'category'] 
        widgets = {
            'due_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'placeholder': 'yyyy-mm-dd hh:mm', 'class': 'form-control'}
            )
        }
