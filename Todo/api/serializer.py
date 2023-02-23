from rest_framework import serializers
from Todo.models import Todo
from rest_framework.exceptions import PermissionDenied


# class TodoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=110)
#     is_done = serializers.BooleanField(default=False)





class TodoSerializer(serializers.ModelSerializer):
    '''
    This Serializer Work With ModelSeializer !
    '''
    class Meta:
        model = Todo
        fields = ('title', 'is_done', 'user', 'id')

