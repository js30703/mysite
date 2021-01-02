import json
from django.db.models import Max
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination


from . jamo1 import A_EOYO
from . models import Verbs, Myverbs
from . serializer import VerbsSerializer, MyverbsSerializer
import random


    
@api_view(['GET'])
@permission_classes([AllowAny])
def snippet_list(request, level):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        max_id = Verbs.objects.all().aggregate(max_id=Max("id"))['max_id'] # method를 임포트함
        i=0
        snippets = []
        
        while i < 4:
            pk1 = random.randint(1, max_id)
            temp = Verbs.objects.get(pk = pk1)
            # if (True) : 
            if (temp.level == level) : 
                snippets += Verbs.objects.filter(pk = pk1)
                i +=1
        serializer = VerbsSerializer(snippets, many=True)
        return Response(serializer.data)


class MyverbsView(viewsets.ModelViewSet):
    queryset = Myverbs.objects.all()
    serializer_class = MyverbsSerializer


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def get_my_verbs(request):

    if request.method == 'GET':
        token = request.headers.get('Authorization')[6:]
        paginator = PageNumberPagination()
        paginator.page_size = 4
        userpk = Token.objects.get(key= token).user.pk
       
        if Myverbs.objects.filter(userpk= userpk).count() == 0 :
            a = Myverbs(userpk= User.objects.get(id=userpk))
            a.save()
            result_page = paginator.paginate_queryset(Verbs,objects.get(id=1), request)
            return paginator.get_paginated_response(VerbsSerializer(result_page, many=True).data )
        else:
            myverbs = Myverbs.objects.get(userpk= userpk).verbList.all()
            result_page = paginator.paginate_queryset(myverbs, request)
            return paginator.get_paginated_response(VerbsSerializer(result_page, many=True).data )

    if request.method == 'POST':
        token = request.headers.get('Authorization')[6:]
        userpk = Token.objects.get(key= token).user.pk
        a = Verbs.objects.get(pk=request.data['id'])
        b = Myverbs.objects.get(userpk= userpk).verbList.add(a)
        Myverbs.objects.get(userpk= userpk).save()
        return Response('successfully added1212.')
        
    if request.method == 'DELETE':
        token = request.headers.get('Authorization')[6:]
        userpk = Token.objects.get(key= token).user.pk
        a = Verbs.objects.get(pk=request.data['id'])
        print(a)
        Myverbs.objects.get(userpk= userpk).verbList.remove(a)
        return Response('successfully deleteed.')

@api_view(['POST'])
@permission_classes([AllowAny])
def check_username(request):
    if request.method == 'POST':
        username = request.data['username']
        print(request.data)
        if (User.objects.filter(username = username).count() == 1):
            return Response({
                "use":False,
                "message":f'{username} is already existed'
                })
        else:
            return Response({
                "use":True,
                "message":f'you can use {username}'
                })