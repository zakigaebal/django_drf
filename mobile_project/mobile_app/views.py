from django.shortcuts import render
from rest_framework import viewsets
from mobile_app.models import humanInfo, Accounts
from mobile_app.serializers import humanInfoSerializer, AccountsSerializer

# Create your views here.

class hInfoViewSet(viewsets.ModelViewSet):
    # queryset에 humanInfo 클래스에 있는 모든 정보를 담기
    queryset = humanInfo.objects.all()
    # serializer_class는 humanInfoSerializer를 이용
    serializer_class = humanInfoSerializer
    
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
    
class CheckAccountViewset(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

    def create(self, request):
        checkID = post_data['checkID']
        checkPW = post_data['checkPW']

        if Accounts.objects.filter(identify=checkID).exists():
            if Accounts.objects.filter(password=checkPW).exists():
                return Response(status=200)

        return Response(status=400)