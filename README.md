# mysite

#  파이썬 장고 시작 2021-04-01
  - https://wikidocs.net/72377
  - 개발서버 구동하기 :    (mysite) C:\projects\mysite>   python manage.py runserver

# 장고 기본 앱 생성  2021-04-02 
  - django-admin의 startapp 명령을 이용하여 pybo 앱을 생성
  > (mysite) C:\projects\mysite>django-admin startapp pybo

# 슈퍼유저 생성 하기 
 - (mysite) c:\projects\mysite>python manage.py createsuperuser
사용자 이름 (leave blank to use 'pahke'): admin
이메일 주소: admin@mysite.com
Password:
Password (again):
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
비밀번호가 너무 일상적인 단어입니다.
비밀번호가 전부 숫자로 되어 있습니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
   
# 장고 Admin에 접속해 로그인하기
 ; 장고 개발 서버를 구동한 후 
  - localhost:8000/admin

# makemigrations로 테이블 작업 파일 생성하기
테이블 작업 파일을 만들려면 makemigrations 명령을 실행해야 하기 때문이다. makemigrations 명령을 먼저 실행
[명령 프롬프트]

(mysite) c:\projects\mysite>python manage.py makemigrations
   
# migrate로 테이블 생성하기
테이블을 생성을 위해 migrate 명령을 실행하자.
[명령 프롬프트]
(mysite) C:\projects\mysite>python manage.py migrate

