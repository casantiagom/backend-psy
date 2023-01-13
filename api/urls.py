from django.urls import path
from . import views

urlpatterns = [
   path('', views.getRoutes, name="routes"),
   path('persons/', views.getPersons, name="persons"),
   path('choices/', views.getChoices, name="choices"),
   path('rankingname/', views.getRankingNames, name="RankingName"),
   path('rankinganswer/', views.getRankingAnswer, name="RankingAnswer"),
   path('rankinganswer/<str:pk>/update/', views.updateRankingAnswer, name="update-rankingAnswer"),
   path('questionlikert/', views.getQuestionLikert, name="questionlikert"),
   path('quizzes/', views.getQuizzes, name="quizzes"),
   path('quizzes/update/', views.updateQuestionLikert, name="update-question"),
   path('answer/', views.getAnswer, name="answer"),
   path('answer/<str:pk>/update/', views.updateAnswer, name="update-answer")
]
