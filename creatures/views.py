from django.http import HttpResponse
from django.template import loader
from .models import Monster
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *

def index(request):
    all_monsters_list = Monster.objects.order_by('-name')
    monster_template = loader.get_template('monsters/index.html')
    context = {
        'all_monsters_list': all_monsters_list,
    }
    #output = ', '.join([i.name for i in all_monsters_list])
    return HttpResponse(monster_template.render(context, request))
    

def monster(request, name):
    try:
        monster = Monster.objects.get(name=name)
    except Monster.DoesNotExist:
        raise Http404()
    context = {
        'monster': monster,
    }
    card_template = loader.get_template('monsters/monster_card.html')

    #return HttpResponse(response + name)
    return HttpResponse(card_template.render(context, request))

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

class monsterList(generics.ListCreateAPIView):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    def post(self,request):
        serializer = MonsterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
