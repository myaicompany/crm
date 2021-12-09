# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
 
 
class Persons(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Агент")
    avat = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото пользователя", null=True, blank=True)
    phon = models.CharField(max_length=15, verbose_name="Телефон",                          null=True, blank=True)
    orga = models.ForeignKey('Organ', on_delete=models.PROTECT, verbose_name="Организация", null=True, blank=True)
 
    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Organ(models.Model):
    titl = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, verbose_name="slug", blank=True)
    desc = models.TextField(verbose_name="Описание", blank=True)
    time_crea = models.DateTimeField(auto_now_add=True)
    time_upda = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titl
        
    # def get_absolute_url(self):
    #     return reverse('home', kwargs={'slug': 'org', 'id': self.pk})

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организация'
        ordering = ['titl']