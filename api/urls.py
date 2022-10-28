from django.urls import path
from . import views

urlpatterns = [
   path('', views.getRoutes, name="routes"),
   path('persons/', views.getPersons, name="persons"),
   path('quizzes/', views.getQuizzes, name="quizzes"),
   path('questionlikert/', views.getQuestionLikert, name="questionlikert"),
   path('quizzes/update/', views.updateQuestionLikert, name="update-question"),
   path('answer/', views.getAnswer, name="answer"),
   path('answer/<str:pk>/update/', views.updateAnswer, name="update-answer")
]
