from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Choice, Question, User


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['question_text']}),
        ('Date information',{'fields': ['pub_date'],'classes':['collapse']}), 
    ]
    inlines =[ChoiceInLine]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    

class CustomUserAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Question, QuestionAdmin)
admin.site.register(User, CustomUserAdmin)
# Register your models here.
