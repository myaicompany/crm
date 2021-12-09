from django import template
from django.contrib.auth.models import User
from django.http import request

from home.models import *


register = template.Library()


@register.simple_tag()
def mmenu():
    mmenu = [
        { 'title': 'Разместить заказ', 'img': 'home/images/add.png', 'url': 'add', 'class': 'add', 'rul':'' },
        { 'title': 'Список заказов',   'img': 'home/images/lst.png', 'url': 'lst', 'class': 'all', 'rul':'' },
        { 'title': 'Отчёты',           'img': 'home/images/rpt.png', 'url': 'rpt', 'class': 'all', 'rul':'man' },
        { 'title': 'Личный кабинет',   'img': 'home/images/per.png', 'url': 'per', 'class': 'all', 'rul':'' },
    ]
    return mmenu



@register.simple_tag()
def infos():
    return Infos.objects.all()



@register.simple_tag(takes_context=True)
def user_groups(context):
    request = context['request']
    groups = ''
    i =''
    for g in request.user.groups.all():
        if groups != '': i = ' и '
        groups = groups + i + str(g)
    return groups



@register.simple_tag(takes_context=True)
def user_orga(context):
    request = context['request']
    info = User.objects.get(id=request.user.id)
    orga = info.persons.orga
    return orga



@register.simple_tag(takes_context=True)
def is_manager(context):
    request = context['request']
    groups =  []
    for g in request.user.groups.all():
        groups.append(g.name)
    
    if 'Менеджеры' in groups:
        return True
    else:
        return False