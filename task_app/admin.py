from django.contrib import admin
from .models import TaskModel
# Register your models here.

class TaskModelAdmin(admin.ModelAdmin) : 
    list_display = ('taskTitle' , 'taskDescription' , 'is_completed' , 'create_at' , 'due_date' , 'priority' ,'category',)
    
admin.site.register(TaskModel, TaskModelAdmin)