
from django.shortcuts import render
from django.http import response, HttpResponse, HttpResponseNotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AnswerSerializer, PersonSerializer, QuestionLikertSerializer, QuizzesSerializer
from .models import Person, Quizzes, QuestionLikert, Answer
from api import serializers
from .utils import createAnswer, getAnswerList, updateAnswerPut
from django.views import View
import os


@api_view(['GET'])
def getRoutes(request):

  routes = [
    {
       'Endpoint': '/persons/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of persons'
    },
    {
       'Endpoint': '/quizzes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of questions'
    },
     {
       'Endpoint': '/questionlikert/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of questions'
    },
     {
       'Endpoint': '/quizzes/update/',
            'method': 'PUT',
            'body': None,
            'description': 'Put likert selection'
    },
     {
       'Endpoint': '/answer/',
            'method': 'GET',
            'body': None,
            'description': 'get array of answers'
    },
    {
       'Endpoint': '/answer/',
            'method': 'POST',
            'body': {'question': ""},
            'description': 'create entry'
    },
      {
       'Endpoint': '/answer/id/update',
            'method': 'PUT',
            'body': {'answerupdate': ""},
            'description': 'get array of answers'
    }

  ]
  return Response(routes)


@api_view(['GET', 'POST'])
def getPersons(request):
  persons = Person.objects.all()
  serializer = PersonSerializer(persons, many=True)
  return Response(serializer.data)

@api_view(['GET','POST'])
def getAnswer(request):
   if request.method == 'GET':
        return getAnswerList(request)

   if request.method == 'POST':
        return createAnswer(request)

@api_view(['PUT'])
def updateAnswer(request,pk):
  return updateAnswerPut(request, pk)

@api_view(['GET', 'POST'])
def getQuizzes(request):
  quizzes = Quizzes.objects.all()
  serializer = QuizzesSerializer(quizzes, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getQuestionLikert(request):
  questionLikert = QuestionLikert.objects.all()
  serializer = QuestionLikertSerializer(questionLikert, many=True)
  return Response(serializer.data)

@api_view(['PUT'])
def updateQuestionLikert(request):
  data = request.data
  questionLikert = QuestionLikert.objects.get()
  serializer = QuestionLikertSerializer(instance=questionLikert, data=data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)


   # if request.method == 'GET':
   #     return getPersonList(request)

   # if request.method == 'POST':
    #    return createPerson(request)

class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()













"""""
class CreatePersonView(APIView):
  serializer_class = CreatePersonSerializer
  def post(self, request, format=None):   
    if not self.request.session.exists(self.request.session.session_key):
      self.request.session.create()

    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      first_name = serializer.data.get('first_name')
      last_name = serializer.data.get('last_name')
      gender = serializer.data.get('gender')
      birthday = serializer.data.get('birthday')
      client_ID = self.request.session.session_key
      queryset = Person.objects.filter(client_ID=client_ID)
      if queryset.exists():
        person = queryset[0]
        person.first_name = first_name
        person.last_name = last_name
        person.gender = gender
        person.birthday = birthday
        person.save(update_fields=['gender', 'birthday'])
        return Response(PersonSerializer(person).data, status=status.HTTP_200_OK)

      else:
        person = Person(client_ID=client_ID, gender=gender, birthday=birthday, first_name=first_name, last_name=last_name)
        person.save()
      return Response(PersonSerializer(person).data,status=status.HTTP_201_CREATED)

    return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)



    from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer, LikertSerializer,CreatePersonSerializer
from .models import Person, Likert

class PersonView(generics.CreateAPIView):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer

class LikertView(generics.CreateAPIView):
  queryset = Likert.objects.all()
  serializer_class = LikertSerializer

class CreatePersonView(APIView):
  serializer_class = CreatePersonSerializer
  def post(self, request, format=None):   
    if not self.request.session.exists(self.request.session.session_key):
      self.request.session.create()

    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      first_name = serializer.data.get('first_name')
      last_name = serializer.data.get('last_name')
      gender = serializer.data.get('gender')
      birthday = serializer.data.get('birthday')
      client_ID = self.request.session.session_key
      queryset = Person.objects.filter(client_ID=client_ID)
      if queryset.exists():
        person = queryset[0]
        person.first_name = first_name
        person.last_name = last_name
        person.gender = gender
        person.birthday = birthday
        person.save(update_fields=['gender', 'birthday'])
        return Response(PersonSerializer(person).data, status=status.HTTP_200_OK)

      else:
        person = Person(client_ID=client_ID, gender=gender, birthday=birthday, first_name=first_name, last_name=last_name)
        person.save()
      return Response(PersonSerializer(person).data,status=status.HTTP_201_CREATED)

    return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

    """