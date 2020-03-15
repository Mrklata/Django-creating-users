from django.db import models


class LangDescription(models.Model):
    LANGUAGE = (('Python', 'Python'),
                ('HTML', 'HTML'),
                ('Django', 'Django'),
                ('CSS', 'CSS'),
                )
    selection = models.CharField(max_length=100, choices=LANGUAGE, default='HTML')
    name = models.CharField(max_length=100)
    description = models.TextField(help_text='skill description')
    libs = models.TextField(help_text='name libraries', default='Some of libraries')
