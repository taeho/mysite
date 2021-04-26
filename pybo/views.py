from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Question

#Question 모델을 임포트해 Question 모델 데이터를 작성한 날짜의 역순으로 조회하기 위해 order_by 함수를 사용
def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    # 조회한 Question 모델 데이터를 템플릿 파일을 사용하여 화면에 출력할 수 있는 render 함수를 사용

# detail 함수의 매개변수 question_id가 추가된 점이 다르다. 바로 이것이 URL 매핑에 있던 question_id
def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # 존재하지 않는 페이지에 접속하면 오류 대신 404 페이지를 출력하도록 detail 함수를 수정
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

# form 엘리먼트에 입력된 값을 받아 데이터베이스에 저장할 수 있도록 answer_create 함수를 추가
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    # 답변을 생성한 후 상세 화면을 호출하려면 redirect 함수를 사용하여 코드를 작성
    return redirect('pybo:detail', question_id=question.id)