import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser

class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?'
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
# Create your models here.
class Empresa(models.Model):
    location = models.CharField(max_length=30, blank=True)
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class User(AbstractUser):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)
    localizacion = models.CharField(max_length=30, blank=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=30,blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username
