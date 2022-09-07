from os import stat
from telnetlib import STATUS
from django.shortcuts import render
from rest_framework import viewsets
from mobile_app.models import humanInfo, Accounts 
from mobile_app.serializers import humanInfoSerializer, AccountsSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response



# Create your views here.

class hInfoViewSet(viewsets.ModelViewSet):
    # queryset에 humanInfo 클래스에 있는 모든 정보를 담기
    queryset = humanInfo.objects.all()
    # serializer_class는 humanInfoSerializer를 이용
    serializer_class = humanInfoSerializer
    
    
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
    

    
