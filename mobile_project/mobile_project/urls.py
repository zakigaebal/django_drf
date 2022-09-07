"""mobile_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from mobile_app import views
# 라우터 만들기
router = routers.DefaultRouter()
# tests라는 이름으로 humanInfoViewSet에 등록
router.register(r'tests', views.hInfoViewSet)
router.register(r'accounts', views.AccountViewSet)



urlpatterns = [
    # admin/ 이라는 url 주소 통해서 접근하면 admin.site.urls로 접근한다.
    path('admin/', admin.site.urls),
    
   
    
    # mobile_app/ 이라는 url 주소 통해서 접근하여 include('mobile_app.urls')로 접근한다.
    path('mobile_app/',include('mobile_app.urls')),
    
    # 라우터 url도 추가
    path('', include(router.urls)),
    
    
    
]
