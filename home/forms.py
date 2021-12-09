from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.db.models.fields import EmailField
from django.forms import ModelForm, TextInput, Textarea, widgets
from django.contrib.auth.models import User
from django.http import request

from .models import *



class LgnForm(AuthenticationForm):
    username = forms.CharField(label='Логин',  widget=forms.TextInput(attrs={'class': 'inp'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'inp'}))


class RgtForm(UserCreationForm):
    username =  forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'inp'}))
    email =     forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'inp'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'inp'}))
    password2 = forms.CharField(label='Пароль (введите ещё раз)', widget=forms.PasswordInput(attrs={'class': 'inp'}))
    is_active = forms.BooleanField(label='is_active', required=False, initial=False, widget=forms.HiddenInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_active')

