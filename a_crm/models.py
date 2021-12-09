from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.conf import settings


class Items(models.Model):

    phot_with = models.BooleanField(default=False, verbose_name="С фото?", null=True, blank=True)
    
    surn =      models.CharField(max_length=255, verbose_name="Фамилия")
    name =      models.CharField(max_length=255, verbose_name="Имя",      null=True, blank=True)
    midn =      models.CharField(max_length=255, verbose_name="Отчество", null=True, blank=True)
    
    date_birt = models.DateField(verbose_name="Дата рождения умершего", null=True, blank=True)
    date_deat = models.DateField(verbose_name="Дата смерти умершего",   null=True, blank=True)
    date_fune = models.DateField(verbose_name="Дата выдачи заказа",     null=True, blank=True)
    
    code =      models.ForeignKey('Codes',    on_delete=models.PROTECT, verbose_name="Код заказа", null=True, blank=True)
    colo =      models.ForeignKey('Colors',   on_delete=models.PROTECT, verbose_name="Цвет рамки", null=True, blank=True)
    fast =      models.ForeignKey('Fasts',    on_delete=models.PROTECT, verbose_name="Крепление",  null=True, blank=True)
    posi =      models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name="Ориентация", null=True, blank=True)
    addr =      models.ForeignKey('Address',  on_delete=models.PROTECT, verbose_name="Адрес",      null=True, blank=True)
    
    numb =      models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Количество",    null=True, blank=True)

    desc =      models.TextField(verbose_name="Рекомендации по обработке", blank=True, help_text='help_text')
    
    phot_natu = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото",                null=True, blank=True)
    phot_reto = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото ретушированное", null=True, blank=True)
        
        
    mana =      models.ForeignKey(User, on_delete=models.PROTECT, related_name = 'mana', verbose_name="Менеджер", null=True, blank=True)

    agre =      models.BooleanField(default=False, verbose_name="Согласовано")
    fini =      models.BooleanField(default=False, verbose_name="Закончен")
    
    auth =      models.ForeignKey(User, on_delete=models.PROTECT, related_name = 'auth', verbose_name="Агент")
    time_crea = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_upda = models.DateTimeField(auto_now=True,     verbose_name="Время изменения")

    def __str__(self):
        return self.surn

    def get_absolute_url(self):
        return reverse('itm', kwargs={'itm_id': self.pk})

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
        ordering = ['-time_crea', 'surn']

    def delete(self, *args, **kwargs):
        super(Items, self).delete(*args, **kwargs)
        try:
            storage, path = self.phot_natu.storage, self.phot_natu.path
            storage.delete(path)
        except:
            pass
        try:
            storage, path = self.phot_reto.storage, self.phot_reto.path
            storage.delete(path)
        except:
            pass


class Address(models.Model):
    titl = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, verbose_name="slug", blank=True)
    desc = models.TextField(verbose_name="Описание", blank=True)
    time_crea = models.DateTimeField(auto_now_add=True)
    time_upda = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titl
        
    class Meta:
        verbose_name = 'Адреса'
        verbose_name_plural = 'Адреса'
        ordering = ['titl']


class Codes(models.Model):

    titl = models.CharField(max_length=255, verbose_name="Заголовок")
    
    slug = models.CharField(max_length=255, verbose_name="slug",                       null=True, blank=True)
    desc = models.TextField(verbose_name="Описание",                                   null=True, blank=True)
    
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена",   null=True, blank=True)
    
    word = models.CharField(max_length=255, verbose_name="Текстовое отображение цены", null=True, blank=True)

    phot = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото",         null=True, blank=True)
    
    time_crea = models.DateTimeField(auto_now_add=True)
    time_upda = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titl
        
    # def get_absolute_url(self):
    #     return reverse('tlsitm', kwargs={'slug': 'cds', 'id': self.pk})

    class Meta:
        verbose_name = 'Коды'
        verbose_name_plural = 'Коды'
        ordering = ['titl']


class Colors(models.Model):
    titl = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, verbose_name="slug", blank=True)
    desc = models.TextField(verbose_name="Описание", blank=True)
    code = models.ForeignKey('Codes', on_delete=models.PROTECT, verbose_name="Код заказа")
    time_crea = models.DateTimeField(auto_now_add=True)
    time_upda = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titl
        
    # def get_absolute_url(self):
    #     return reverse('tlsitm', kwargs={'slug': 'clr', 'id': self.pk})

    class Meta:
        verbose_name = 'Цвета'
        verbose_name_plural = 'Цвета'
        ordering = ['titl']


class Fasts(models.Model):
    titl = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, verbose_name="slug", blank=True)
    desc = models.TextField(verbose_name="Описание", blank=True)
    code = models.ForeignKey('Codes', on_delete=models.PROTECT, verbose_name="Код заказа")
    time_crea = models.DateTimeField(auto_now_add=True)
    time_upda = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titl
        
    # def get_absolute_url(self):
    #     return reverse('tlsitm', kwargs={'slug': 'fst', 'id': self.pk})

    class Meta:
        verbose_name = 'Крепеж'
        verbose_name_plural = 'Крепеж'
        ordering = ['titl']


class Position(models.Model):
    titl = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, verbose_name="slug", blank=True)
    desc = models.TextField(verbose_name="Описание", blank=True)
    code = models.ForeignKey('Codes', on_delete=models.PROTECT, verbose_name="Код заказа")
    time_crea = models.DateTimeField(auto_now_add=True)
    time_upda = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titl
        
    # def get_absolute_url(self):
    #     return reverse('home', kwargs={'slug': 'pst', 'id': self.pk})

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиция'
        ordering = ['titl']





