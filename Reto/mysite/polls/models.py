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
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
# Create your models here.

class User(AbstractUser):
    name = models.TextField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.TextField(max_length=50,blank=True)
    
    def __str__(self):
        return self.name

