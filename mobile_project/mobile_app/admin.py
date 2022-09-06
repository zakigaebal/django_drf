from django.contrib import admin

# Register your models here.

# 모델 불러오기
from mobile_app.models import humanInfo,Accounts

# 장고 서버에 모델 등록하기
admin.site.register(humanInfo)
admin.site.register(Accounts)