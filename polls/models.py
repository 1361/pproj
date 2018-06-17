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
    unit = models.CharField(max_length=50, default="")
    list_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.type


class Cart(models.Model):
    products = models.ForeignKey(Products, null=False)
    quantity = models.IntegerField(default=0)


class Order(models.Model):
    cart = models.ForeignKey(Cart)
    charge_id = models.CharField(max_length=400)
    user = models.ForeignKey(User)
    shipping_address = models.CharField(max_length=200)
    order_date = models.DateTimeField('Date Ordered')
