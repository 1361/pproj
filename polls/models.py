from django.db import models


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Car(models.Model):
    name = models.CharField(max_length=234)
    year = models.CharField(max_length=4)
    charge_id = models.CharField(max_length=234)
