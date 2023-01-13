from django.contrib import admin
from . import models

@admin.register(models.Person)

class Person(admin.ModelAdmin):
	list_display = ['last_name','first_name','id']
	readonly_fields = ['id']



class QuestionInlineModel(admin.TabularInline):
    model = models.QuestionLikert
    

class PersonInlineModel(admin.TabularInline):
    model = models.Person.quizzes.through
    extra = 1


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'title',
        ]
    inlines = [
        QuestionInlineModel,
        PersonInlineModel
        ]
    exclude = ( 'quizzes',)

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    

@admin.register(models.QuestionLikert)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'question',
        'quiz',
        ]
    list_display = [
        'question', 
        'quiz',
        'date_updated'
        ]
    inlines = [
        AnswerInlineModel, 
        ] 

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer', 
        'question',
        'person'
        ]


class ChoicesInlineModel(admin.TabularInline):
    model = models.Choice


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id', 
        ]
    


@admin.register(models.RankingName)
class RankingNamesAdmin(admin.ModelAdmin):
    fields = [
        'choice',
        'rankingName',
        ]
   
    

@admin.register(models.RankingAnswer)
class RankingAnswerAdmin(admin.ModelAdmin):
    list_display = [
        'choice', 
        'userChoice',
        'person'
        ]
    