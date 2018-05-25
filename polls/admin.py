from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Question, Choice, Listing, Products



# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class ProductsInline(admin.TabularInline):
    model = Products
    extra = 3


class ListingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['listing_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ProductsInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Listing, ListingAdmin)

