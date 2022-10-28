from rest_framework.serializers import ModelSerializer
from .models import Person, Quizzes, QuestionLikert, Answer

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'user_email']

class QuizzesSerializer(ModelSerializer):
    class Meta:
        model = Quizzes
        fields = '__all__'      

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'        

class QuestionLikertSerializer(ModelSerializer):
    class Meta:
        model = QuestionLikert
        fields = '__all__'  