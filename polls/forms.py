from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#
class ProducerProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone_number = forms.CharField(max_length=30, required=False, help_text='Optional.')
    address = forms.CharField(max_length=50, required=False, help_text='Optional.')
    operation_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',  'first_name', 'last_name', 'email', 'phone_number', 'address',)


class ConsumerProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone_number = forms.CharField(max_length=30, required=False, help_text='Optional.')
    address = forms.CharField(max_length=50, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',  'first_name', 'last_name', 'email', 'phone_number', 'address',)