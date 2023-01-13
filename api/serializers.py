from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Person, Quizzes, QuestionLikert, Answer, RankingName, Choice, RankingAnswer

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'      

class PersonIdSerializer(serializers.RelatedField):
    def to_representation(self, value):
         return value.id

class QuizzesSerializer(ModelSerializer):
    person = PersonIdSerializer(read_only=True)
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

class ChoiceTextSerializer(serializers.RelatedField):
    def to_representation(self, value):
         return value.title


    

class RankingNameSerializer(ModelSerializer):
    choice = ChoiceTextSerializer(many=True, read_only=True)
    class Meta:
        model = RankingName
        fields = '__all__'

class ChoiceSerializer(ModelSerializer):
    class Meta:
        
        model = Choice
        fields = '__all__'


    
class RankingAnswerSerializer(ModelSerializer):
    choice = serializers.SlugRelatedField(
        queryset=RankingAnswer.objects.all(),
        slug_field='title'
     )
    class Meta:
        model = RankingAnswer
        fields = '__all__'        



        
class RankingAnswerUpdateSerializer(ModelSerializer):
    choice = serializers.CharField(
       source="choice.choice_title", read_only=True
     )
    class Meta:
        model = RankingAnswer
        fields = '__all__'        
