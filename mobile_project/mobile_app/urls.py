from django.urls import path, include, re_path

# 앱 이름
app_name = 'mobile_app'

# path 설정
urlpatterns = [
    path('',include('rest_framework.urls',namespace='rest_framework_category')),
]
