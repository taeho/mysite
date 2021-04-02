"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# 장고가 사용자의 페이지 요청을 이해할 수 있도록 config/urls.py 파일
# config/urls.py 파일은 페이지 요청 시 가장 먼저 호출되며, 요청 URL과 뷰 함수를 1:1로 연결"

from django.contrib import admin
# ---------------------------------- [edit] ---------------------------------- #
from django.urls import path, include
# ---------------------------------------------------------------------------- #

urlpatterns = [
    path('admin/', admin.site.urls),
# ---------------------------------- [edit] ---------------------------------- #
    path('pybo/', include('pybo.urls')),
# ---------------------------------------------------------------------------- #
]