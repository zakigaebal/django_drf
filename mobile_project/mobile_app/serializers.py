# restFrameWork에서 사용하는 기능
# 우리가 만든 데이터 모델과 1:1 형태로 (Json으로) 매칭 시켜줌

from dataclasses import field
from rest_framework import serializers
from .models import Accounts, humanInfo

# 시리얼라이저에 있는 모델 시리얼라이저를 확장시킨 클래스
class humanInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        # 모델명은 humanInfo
        model = humanInfo
        # humanInfo에서 created를 제외한 나머지 필드만 Json파일로 바꿔주기
        fields = ['name','phone_number','address']
        
class AccountsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Accounts
        field = ('identify','password')