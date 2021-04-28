from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import QuestionForm, AnswerForm
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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            # 답변을 생성한 후 상세 화면을 호출하려면 redirect 함수를 사용하여 코드를 작성
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

# question_create 함수는 QuestionForm 클래스로 생성한 객체 form을 사용
# 여기서 QuestionForm 클래스는 질문을 등록하기 위해 사용하는 장고의 폼이다.
# render 함수에 전달한 {'form': form}은 템플릿에서 폼 엘리먼트를 생성할 때 사용
def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # form으로 Question 모델 데이터를 저장하기 commit=False는 임시 저장을 의미
            # 임시 저장을 사용하는 이유는 폼으로 질문 데이터를 저장할 경우
            # Question 모델의 create_date에 값이 설정되지 않아 오류가 발생하기 때문에
            # 임시 저장을 한 후 question 객체를 반환받아 create_date에 값을 설정한 후 question.save()로 실제 저장
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)