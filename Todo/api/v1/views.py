from rest_framework.response import Response
from rest_framework.decorators import api_view
from Todo.api.serializer import TodoSerializer
from Todo.models import Todo
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        object_list = Todo.objects.all()
        serializer = TodoSerializer(object_list, many=True) 
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

@api_view()
def todo_detail(request, pk):
    todo_object = get_object_or_404(Todo, id=pk)
    serializer = TodoSerializer(todo_object)
    return Response(data=serializer.data, status=status.HTTP_200_OK)