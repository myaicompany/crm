from django.http.response import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView, UpdateView 
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import *

from .models import *
from .forms import *
from a_crm.models import Codes




class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
    login_url = reverse_lazy('lgn')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Start'
        return context



# Information -------------------

class InfLst(LoginRequiredMixin, ListView):
    model = Infos
    template_name = 'home/inflst.html'
    context_object_name = 'info'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все заказы'
        return context
    
    def get_queryset(self):
        return Infos.objects.all()


class InfOne(LoginRequiredMixin, DetailView):
    model =Infos
    template_name = 'home/infone.html'
    pk_url_kwarg = 'inf_id'
    context_object_name = 'info'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['info']
        return context


# class AboutCodes(LoginRequiredMixin, TemplateView):

#     model = Codes
#     template_name = 'home/aboutcodes.html'
#     pk_url_kwarg = 'cds_id'
#     context_object_name = 'info'
#     login_url = reverse_lazy('lgn')

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Описание кодов'
#         return context

def aboutcodes(request):

    data = Codes.objects.all()

    context = {
        'title': 'Описание кодов',
        'data': data,
    }

    return render(request, 'home/aboutcodes.html', context)



# Persons ----------------

class Lgn(LoginView):
    form_class = LgnForm
    template_name = 'home/lgn.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context
    
    def get_success_url(self):
        return reverse_lazy('home')


class Rgt(CreateView):
    form_class = RgtForm
    template_name = 'home/rgt.html'
    success_url = reverse_lazy('lgn')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация нового пользователя"
        return context


def lgt(request):
    logout(request)
    return redirect('lgn')


def pageNotFound(request, exeption):
    return HttpResponseNotFound("hehe")
