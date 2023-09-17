from django.contrib.auth.models import User
from django.db import models

# Create your models here.
    
class TaskModel(models.Model):
    PRIORITY_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    )
    CATEGORY_CHOICES = (
        ('homework' , 'HOMEWORK'),
        ('bazar' , 'BAZAR'),
        ('study_routine' , 'STUDY_ROUTINE')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=0)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES ,default='HOMEWORK')
    
    def __str__(self):
        return self.taskTitle
    class Meta:
        order_with_respect_to = 'user'
