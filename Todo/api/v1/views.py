from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from Todo.api.serializer import TodoSerializer
from Todo.models import Todo
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def todo_list(request):
    if request.method == 'GET':
        print(request.user)
        todo_list = Todo.objects.get_all_todo_by_user(user=request.user)
        serializer = TodoSerializer(todo_list, many=True) 
        return Response(data=serializer.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    todo_object = get_object_or_404(Todo, id=pk)
    if request.method == 'GET': 
        serializer = TodoSerializer(todo_object)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        response = {
            'detail': 'todo object Is Deleted Successfully',
            'id': todo_object.id ,
            'title': todo_object.title,
            'user': todo_object.user.id
        }
        todo_object.delete()
        return Response(response, status=status.HTTP_204_NO_CONTENT)