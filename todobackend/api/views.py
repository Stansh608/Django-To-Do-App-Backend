from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task

from .serializers import TaskSerializer
# Create your views here.

#get tasks
@api_view(['GET'])
def taskView(request):
    tasks=Task.objects.all()
    # serialize the data
    serializer=TaskSerializer(tasks, many=True)
    return Response(serializer.data)

#task details
@api_view(['GET'])
def taskDetail(request, pk):
    task=Task.objects.get(pk=pk)
    serializer=TaskSerializer(task, many=False)
    return Response(serializer.data)

#add task
@api_view(['POST'])
def postTask(request):
    
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update task
@api_view(['POST'])
def updateTask(request,pk):
    task=Task.objects.get(pk=pk)
    serializer=TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete Task
@api_view(['DELETE'])
def deleteTask(request, pk):
    task=Task.objects.get(pk=pk)
    task.delete()
    
    return Response("Task deleted Successfully!!")