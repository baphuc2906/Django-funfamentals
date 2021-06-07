import datetime
from django.utils import timezone

from django.db import models

# Create your models here.


class Question(models.Model):
    question_test = models.CharField(max_length=255)
    pub_date = models.DateTimeField('Date publised')

    def __str__(self):
        return self.question_test

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    DoesNotExist = None
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

