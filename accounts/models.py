from django.db import models
from django.urls import reverse


class LangDescription(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(help_text='skill description')
    libs = models.TextField(help_text='name libraries', default='Some of libraries')
    image = models.ImageField(upload_to='media', null=True)

    class Meta:
        verbose_name = 'Umiejętność'
        verbose_name_plural = 'Umiejętności'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('skill', kwargs={'name': self.name})
