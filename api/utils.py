from rest_framework.response import Response
from .models import  Answer, Person, QuestionLikert, Quizzes, Choice, RankingAnswer
from .serializers import AnswerSerializer, PersonSerializer, QuestionLikertSerializer, QuizzesSerializer, ChoiceSerializer, RankingAnswerSerializer, RankingAnswerUpdateSerializer


def getPersonList(request):
    person = Person.objects.all().order_by('-last_name')
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)

def createPerson(request):
    data = request.data
    person = Person.objects.create(
        body=data['body']
    )
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)

# ANSWERS

def getAnswerList(request):
  answer = Answer.objects.all()
  serializer = AnswerSerializer(answer, many=True)
  return Response(serializer.data)  

def createAnswer(request):
    data = request.data
    answer = Answer.objects.create(question=QuestionLikert.objects.get(id=data['question']),answer=data['answer'], person=Person.objects.get(id=data['person']))
    serializer = AnswerSerializer(answer, many=False)
    return Response(serializer.data)

def updateAnswerPut(request, pk):
    data = request.data
    answer = Answer.objects.get(id=pk)
    serializer = AnswerSerializer(answer, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#RANKING ANWSER

def getRankingAnswerList(request):
  rankingAnswer = RankingAnswer.objects.all()
  serializer = RankingAnswerSerializer(rankingAnswer, many=True)
  return Response(serializer.data)  

def createRankingAnswer(request):
    data = request.data
    rankingAnswer = RankingAnswer.objects.create(choice=Choice.objects.get(title=data['choice']),userChoice=data['userChoice'], person=Person.objects.get(id=data['person']))
    serializer = RankingAnswerSerializer(rankingAnswer, many=False)
    return Response(serializer.data)

def updateRankingAnswerPut(request, pk):
    data = request.data
    rankingAnswer = RankingAnswer.objects.get(id=pk)
    serializer = RankingAnswerUpdateSerializer(rankingAnswer, partial=True, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#QUIZZES

def getQuizzes(request):
    quizzes = Quizzes.objects.all().order_by('-setName')
    serializer = QuizzesSerializer(quizzes, many=True)
    return Response(serializer.data)

def getQuestionLikert(request):
    questionLikert = QuestionLikert.objects.all().order_by('-question')
    serializer = QuestionLikertSerializer(questionLikert, many=True)
    return Response(serializer.data)

#CHOICES

def getChoices(request):
    choice = Choice.objects.all().order_by('-choice')
    serializer = ChoiceSerializer(choice, many=True)
    return Response(serializer.data)

def createChoice(request):
    data = request.data
    choice = Choice.objects.create(
        body=data['body']
    )
    serializer = ChoiceSerializer(choice, many=True)
    return Response(serializer.data)