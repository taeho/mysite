from django.urls import path

from . import views

# ---------------------------------- [edit] ---------------------------------- #
# pybo/urls.py 파일에 네임스페이스를 추가하려면 간단히 app_name 변수에 네임스페이스 이름을 저장
app_name = 'pybo'
# ---------------------------------------------------------------------------- #

urlpatterns = [
    # 템플릿의 href에 실제 주소가 아니라 URL 별칭을 사용
    # pybo/urls.py 파일에 네임스페이스를 추가하려면 간단히 app_name 변수에 네임스페이스 이름을 저장
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]