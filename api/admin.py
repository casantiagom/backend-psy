from django.contrib import admin
from . import models

@admin.register(models.Person)

class Person(admin.ModelAdmin):
	list_display = ['last_name','first_name','id']
	readonly_fields = ['id']



class QuestionInlineModel(admin.TabularInline):
    model = models.QuestionLikert
    

@admin.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'title',
        'person'
        ]
    inlines = [
        QuestionInlineModel, 
        ] 

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