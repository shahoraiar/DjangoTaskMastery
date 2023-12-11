from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views 
urlpatterns = [
    path('add_task/' , views.task_form.as_view() , name = "taskform") , #task/
    path('sort_tasks/<str:sort_option>/', views.sort_tasks, name='sort_tasks'),
    path('task_show/' , views.task_show , name = "show_task") ,
    path('delete/<int:pk>' , views.delete_task.as_view() , name = "delete") ,
    path('edit/<int:pk>' , views.edit_task.as_view() , name = "edit") ,
    path('mark_complete/<int:id>' , views.mark_completed , name ="mark_complete"),
    path('completed/' , views.completed , name='completed'),
    
    path('api/', views.TaskApiList.as_view(),name='api'),
    path('api/<int:pk>/', views.TaskApiDetail.as_view(),name="api_details"),
]
