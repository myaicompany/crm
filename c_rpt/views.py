from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.aggregates import Avg, Sum
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView, ListView

from a_crm.models import *
from datetime import datetime


class Rpt(LoginRequiredMixin, ListView ):
    model = Items
    template_name = 'c_rpt/rpt.html'
    context_object_name = 'data'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все заказы'
        return context
    
    def get_queryset(self):
        day = datetime.now()
        time = self.request.GET.get('time')
        if time == 'day':
            return Items.objects.filter(auth=self.request.user, time_crea__in=[day])



def rpt(request):
    
    title = 'Отчет агента'
    subtitle = 'Выберите период отчёта'
    point1 = ''
    point2 = ''
    data = ''
    totalcoun = 0
    totalcost = 0

    if request.method == 'POST':
        period = request.POST.get('period')

        if period == 'day':
            point1 = datetime.now().date()
            point2 = datetime.now().date()
            subtitle = 'Текущий отчёт за день ' + str(point1.strftime("%d.%m.%Y"))
            data = Items.objects.filter(auth=request.user)
            data = data.filter(time_crea__gte=point1)
            totalcoun = data.count
            
        if period == 'mou':
            point1 = datetime.now().date().replace(day=1)
            point2 = datetime.now().date()
            subtitle = 'Текущий отчёт за месяц с ' + str(point1.strftime("%d.%m.%Y"))
            data = Items.objects.filter(auth=request.user)
            data = data.filter(time_crea__gte=point1)
            totalcoun = data.count
            
        if period == 'cus':
            point1 = request.POST.get('point1')
            point2 = request.POST.get('point2')

            # point1 = datetime.strptime(point1, "%Y-%m-%d")
            # point2 = datetime.strptime(point2, "%Y-%m-%d")

            if point1 == '' or point2 == '':
                subtitle = 'Уточните дату'
            else:
                subtitle = 'Отчёт за период с ' + point1 + ' по ' + point2
                data = Items.objects.filter(auth=request.user)
                data = data.filter(time_crea__gte=point1, time_crea__lte=point2)
                totalcoun = data.count

        for d in data:
            if d.code:
                cost = d.code.cost
                totalcost += cost

    context = {
        'title': title,
        'subtitle': subtitle,
        'point1': point1,
        'point2': point2,
        'data': data,
        'totalcoun': totalcoun,
        'totalcost': totalcost,
    }

    return render(request, 'c_rpt/rpt.html', context)



@login_required(login_url='/lgn')
def exe(request):

    info = 'info'
        
    context = {
        'title': 'Эксперимент',
        'info': info,
    }

    return render (request, 'b_per/exe.html', context)
