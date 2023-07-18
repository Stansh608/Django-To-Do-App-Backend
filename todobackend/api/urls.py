from django.urls import path
from . import views

#URL endpoints
urlpatterns = [
    # A list of tasks
    path('', views.urlsOverview, name="urls-endpoint"),
    path('task-list', views.taskView, name="task-list"),
    
    path('task-detail/<str:pk>', views.taskDetail, name="task-detail"),
    #add task
    path('task-add/', views.postTask, name="task-add"),
    
    #update Task
    path('task-update/<str:pk>', views.updateTask, name="task-update"),
    
    #Delete TAsk
    path('task-delete/<str:pk>', views.deleteTask, name="task-delete"),
]
