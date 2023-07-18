from django.urls import path
from . import views

#URL endpoints
urlpatterns = [
    # A list of tasks
    path('', views.taskView, name="task-list"),
    
    path('task-detail/<str:pk>', views.taskDetail, name="task-detail"),
    #add task
    path('add-task/', views.postTask, name="add-task"),
    
    #update Task
    path('update-task/<str:pk>', views.updateTask, name="update-task"),
    
    #Delete TAsk
    path('delete-task/<str:pk>', views.deleteTask, name="delete-task"),
]
