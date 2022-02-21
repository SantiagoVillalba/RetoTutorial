from django.contrib import admin
from .models import Choice, Question, User, Empresa
from .logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine


class ChoiceInLine(LogicaLDeletedModelTabularInLine):
    model = Choice
    extra = 3


class QuestionAdmin(LogicalDeletedModelAdmin):
    fieldsets = [
        (None,              {'fields': ['question_text']}),
        ('Date information',{'fields': ['pub_date'],'classes':['collapse']}), 
    ]
    inlines =[ChoiceInLine]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    

class CustomUserAdmin(LogicalDeletedModelAdmin):
    pass 

class CustomEmpresaAdmin(LogicalDeletedModelAdmin):
    pass 

admin.site.register(Question, QuestionAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Empresa, CustomEmpresaAdmin)

