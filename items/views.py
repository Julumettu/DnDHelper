from django.http import HttpResponse
from django.template import loader
from .models import Item
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *

class itemsList(APIView):
    def get(self,request):
        items = Item.objects.all()
        serializer=ItemSerializer(items, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
