from django.db import models
from django.urls.base import reverse


class Infos(models.Model):
    titl = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, verbose_name="slug", blank=True)
    desc = models.TextField(verbose_name="Описание", blank=True)
    cont = models.TextField(verbose_name="Содержание", blank=True)
    time_crea = models.DateTimeField(auto_now_add=True)
    time_upda = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titl
        
    def get_absolute_url(self):
        return reverse('infone', kwargs={'inf_id': self.pk})

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'
        ordering = ['titl']
