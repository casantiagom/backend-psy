from email.policy import default
from django.db import models
from django.utils.timezone import now
import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here.

LIKERT_CHOICES = [('1', 'nada'),('2', 'poco'),('3', 'normal'),('4', 'Harto'), ('5', 'Demasiado')]
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not Applicable')
    )

class Person(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  client_ID =  models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  birthday = models.DateField(null=True)
  user_email = models.EmailField(max_length=70,blank=True, null=True, unique=True)
  

  def __str__(self):
        return self.last_name + " " + self.first_name
  
class Quizzes(models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    person = models.ForeignKey(
        Person, default=1, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):

    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class QuestionLikert(Updated):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']
    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.CASCADE)
    question = models.CharField(max_length=255, verbose_name=_("Question"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))

    def __str__(self):
        return self.question

class Answer(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        QuestionLikert, related_name='answer', on_delete=models.DO_NOTHING)
    answer = models.IntegerField(
        blank=True, verbose_name=_("Answer"))
    person = models.ForeignKey(
        Person, on_delete=models.DO_NOTHING, unique=False)
    answer_text = str(answer)

    def __str__(self):
        return self.answer_text  

  #def __str__(self):
   # return self.last_name + " " + self.first_name

