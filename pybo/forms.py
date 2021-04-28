from django import forms

from pybo.models import Question, Answer

#  장고 폼은 사실 2개의 폼으로 구분할 수 있는데,
#  forms.Form을 상속받으면 폼, forms.ModelForm을 상속받으면 모델 폼이라 부른다.
#  여기서는 form.ModelForm을 상속받아 모델 폼을 만들었다.
#  모델 폼은 말 그대로 모델과 연결된 폼이며, 모델 폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있다.

# ModelForm을 상속받은 QuestionForm 클래스를 작성
# QuestionForm 클래스는 Question 모델과 연결되어 있으며, 필드로 subject, content를 사용한다고 정의
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }