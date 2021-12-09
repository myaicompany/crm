from django.http import request
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView, UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import *

from .models import *



# class Per(LoginRequiredMixin, TemplateView):
#     template_name = 'b_per/per.html'
#     login_url = reverse_lazy('lgn')
#     def get_context_data(self, *, object_list=None, **kwargs):

#         id = 1

#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Личный кабинет'
#         context['info'] = id
#         return context


@login_required(login_url='/lgn')
def per(request):

    info = User.objects.get(id=request.user.id)

    groups = ''
    for g in request.user.groups.all():
        if groups != '': i = ' и '
        else: i =''
        groups = groups + i + str(g)

        
    context = {
        'title': 'Личный кабинет',
        'info': info,
        'groups': groups,
    }

    return render (request, 'b_per/per.html', context)


