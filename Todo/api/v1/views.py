from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def todo_list(request):
    return Response({'status': 'ok'})

@api_view()
def todo_detail(request, pk):
    return Response({'status': '200'})