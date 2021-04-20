from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # /pybo/2/의 숨은 의도는 'Question 모델 데이터 중 id값이 2인 데이터를 조회하라'이다
    path('<int:question_id>/', views.detail),
]