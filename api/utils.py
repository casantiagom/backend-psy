from rest_framework.response import Response
from .models import  Answer, Person, QuestionLikert, Quizzes
from .serializers import AnswerSerializer, PersonSerializer, QuestionLikertSerializer, QuizzesSerializer


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

#QUIZZES

def getQuizzes(request):
    quizzes = Quizzes.objects.all().order_by('-setName')
    serializer = QuizzesSerializer(quizzes, many=True)
    return Response(serializer.data)

def getQuestionLikert(request):
    questionLikert = QuestionLikert.objects.all().order_by('-question')
    serializer = QuestionLikertSerializer(questionLikert, many=True)
    return Response(serializer.data)

