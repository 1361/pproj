from django.db import models
from django.contrib.auth.models import User

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


class Listing(models.Model):
    listing_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.listing_name


class Products(models.Model):
    listing = models.ForeignKey(Listing)
    type = models.CharField(max_length=200)
    amount_available = models.IntegerField(default=0)
    list_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.type

#
# class Orders(models.Model):
#     user = models.ForeignKey(User)
#     listing = models.ForeignKey(Listing)
#     products = models.ForeignKey(Products)
#     quantity = models.IntegerField(default=0)


