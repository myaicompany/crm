from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.db.models.fields import EmailField
from django.db.models.fields.files import FileField
from django.forms import ModelForm, TextInput, Textarea, widgets
from django.contrib.auth.models import User

from django.conf import settings
from django.http import request

from .models import *

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class NewClearableFileInput(widgets.ClearableFileInput):
    template_name = 'django/forms/widgets/new_file_input.html'
    
    def xx(self):
        return '10'


class NewCheckboxInput(widgets.CheckboxInput):
    template_name = 'django/forms/widgets/new_checkbox.html'

    def get_context(self, name, value, attrs, **kwargs):
        context = super().get_context(name, value, attrs, **kwargs)
        context['widget']['on'] = 'В работе'
        context['widget']['of'] = 'Взять в работу'
        return context


class ItmForm(ModelForm):

    phot_with = forms.BooleanField(label='Без фото', required=False, initial=False)

    surn = forms.CharField(label='Фамилия умершего',  widget=TextInput(attrs={'class': 'inp', 'placeholder': 'Фамилия'}))
    name = forms.CharField(label='Имя умершего',      widget=TextInput(attrs={'class': 'inp', 'placeholder': 'Имя'}), required=False)
    midn = forms.CharField(label='Отчество умершего', widget=TextInput(attrs={'class': 'inp', 'placeholder': 'Отчество'}), required=False)
    
    date_birt = forms.DateField(label='Дата рождения умершего', widget=TextInput(attrs={'class': 'inp dates', 'placeholder':'Введите дату' }))
    date_deat = forms.DateField(label='Дата смерти умершего',   widget=TextInput(attrs={'class': 'inp dates', 'placeholder':'Введите дату' }), required=False)
    date_fune = forms.DateField(label='Дата выдачи заказа',     widget=TextInput(attrs={'class': 'inp dates', 'placeholder':'Введите дату' }), required=False)
    
    code = forms.ModelChoiceField(label='Код', queryset=Codes.objects.all(), widget=forms.RadioSelect(attrs={'class': 'rds'}), required=False)
    colo = forms.ModelChoiceField(label='Цвет рамки',     queryset=Colors.objects.all(),   widget=forms.Select(attrs={'class': 'sel'}),      required=False)
    fast = forms.ModelChoiceField(label='Крепёж',         queryset=Fasts.objects.all(),    widget=forms.Select(attrs={'class': 'sel'}),      required=False)
    posi = forms.ModelChoiceField(label='Ориентация',     queryset=Position.objects.all(), widget=forms.Select(attrs={'class': 'sel'}),      required=False)
    addr = forms.ModelChoiceField(label='Адрес доставки', queryset=Address.objects.all(),  widget=forms.Select(attrs={'class': 'sel'}),      required=False)

    numb = forms.DecimalField(label='Количество', widget=forms.NumberInput(attrs={'class': 'inp', 'min':1,'max': '666'}), required=False, initial=1)
    
    desc = forms.CharField(label='Рекомендации по ретуши фотографии',  widget=forms.Textarea(attrs={'class': 'txta', 'placeholder': 'Если вы не заполнили этот раздел, то обработка изображения выполняется в соответствии с стандартами подрядчика'}), required=False, help_text='Если вы не заполнили этот раздел, то обработка изображения выполняется в соответствии с стандартами подрядчика')

    phot_natu = forms.ImageField(label='Загрузить фотографию умершего', widget=NewClearableFileInput(attrs={'class': 'fil'}), required=False)
    phot_reto = forms.ImageField(label='Фото ретушированное',           widget=NewClearableFileInput(attrs={'class': 'fil'}), required=False)
    
    mana_chec = forms.BooleanField(label='Менеджер',    widget=NewCheckboxInput(attrs={'class': 'chx'}), required=False, initial=False)
    
    agre = forms.BooleanField(label='Согласовано', widget=widgets.CheckboxInput(attrs={'class': 'chx'}), required=False, initial=False)  
    fini = forms.BooleanField(label='Выполнен',    widget=widgets.CheckboxInput(attrs={'class': 'chx'}), required=False, initial=False)

    class Meta:
        model = Items
        fields = [
            'phot_with', 
            'surn', 'name', 
            'midn', 
            'date_birt', 
            'date_deat', 
            'date_fune', 
            'code', 
            'numb', 
            'colo', 
            'fast', 
            'posi', 
            'addr', 
            'phot_natu', 
            'phot_reto', 
            'desc',
            'agre',
            'fini',
            'mana',
        ]


class SearForm(forms.Form):
    agent = forms.CharField(widget=TextInput(attrs={'placeholder': 'Поиск по фамлии агента'}))










# class ItmFormChenAge(ItmForm):

#     class Meta:
#         model = Items
#         fields = ['phot_with', 'surn', 'name', 'midn', 'date_birt', 'date_deat', 'date_fune', 'code', 'numb', 'colo', 'fast', 'posi', 'addr', 'phot_natu', 'desc']


# class ItmFormChenMan(ItmForm):

    
    

#     class Meta:
#         model = Items
#         fields = ['phot_with', 'surn', 'name', 'midn', 'date_birt', 'date_deat', 'date_fune', 'code', 'numb', 'colo', 'fast', 'posi', 'addr', 'phot_natu', 'phot_reto', 'desc', 'agre', 'fini']
