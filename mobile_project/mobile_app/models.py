from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class humanInfo(models.Model):
    #이름
    name = models.CharField(max_length=10)
    #핸드폰번호
    phone_number = models.CharField(max_length=13)
    #주소
    address = models.TextField()
    #데이터 생성 날짜(현재시간기준 자동 저장)
    created = models.DateTimeField(auto_now_add=True)
    
    #created 기준 오름차순 정렬
    class Meta : ordering = ['created']
    
    
class Accounts(models.Model):
    identify = models.CharField(default='identify', max_length=20)
    password = models.CharField(default='password',max_length=20)
    
