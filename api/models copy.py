from email.policy import default
from django.db import models
from django.utils.timezone import now
import uuid

# Create your models here.

LIKERT_CHOICES = [('1', 'nada'),('2', 'poco'),('3', 'normal'),('4', 'Harto'), ('5', 'Demasiado')]
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not Applicable')
    )

  
class QuestionLikert(models.Model):
  question = models.CharField(max_length=150 )
  selection = models.CharField(choices=LIKERT_CHOICES, max_length=1, default=3)
  date = models.DateTimeField(default=now, blank=True, editable=False)

  def __str__(self):
    return self.question

class QuestionSet(models.Model):
  setName = models.CharField(max_length=50)
  question_likert = models.ManyToManyField(QuestionLikert, null=True, blank=True)

  def __str__(self):
    return self.setName


class Person(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  client_ID =  models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  birthday = models.DateField(null=True)
  questionSet = models.ManyToManyField(QuestionSet, null=True, blank=True)

  #def __str__(self):
   # return self.last_name + " " + self.first_name

