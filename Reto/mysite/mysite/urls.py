
from typing import List

from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI
from polls.models import *
from ninja import ModelSchema

api = NinjaAPI()

class UserSchema(ModelSchema):

    class Config:
        model = User
        model_fields = "__all__"

class QuestionSchema(ModelSchema):

    class Config:
        model = Question
        model_fields = "__all__"

class ChoiceSchema(ModelSchema):

    class Config:
        model = Choice
        model_fields = "__all__"

class EmpresaSchema(ModelSchema):

    class Config:
        model = Empresa
        model_fields = "__all__"

@api.get("/user/{int:id}",response = UserSchema)
def userGet(request,id):
    user = User.objects.filter(pk=id).first() # [0]
    return user

@api.get("/users",response = List[UserSchema])
def usersGet(request):
    users = User.objects.all()
    return users

@api.get("/questions",response = List[QuestionSchema])
def questionsGet(request):
    questions = Question.objects.all()
    return questions

@api.get("/question/{int:id}",response = QuestionSchema)
def questionGet(request,id):
    question = Question.objects.filter(pk=id).first()
    return question

@api.get("/choices",response = List[ChoiceSchema])
def choicesGet(request):
    choices = Choice.objects.all()
    return choices

@api.get("/choice/{int:id}",response = ChoiceSchema)
def choiceGet(request,id):
    choice = Choice.objects.filter(pk=id).first()
    return choice

@api.get("/questionChoices/{int:id}",response = List[ChoiceSchema])
def questionChoices(request,id):
    question = Question.objects.filter(pk=id).first()
    choices = question.choice_set
    return choices

@api.get("/choiceQuestion/{int:id}",response = QuestionSchema)
def choiceQuestion(request,id):
    choice = Choice.objects.filter(pk=id).first()
    question = choice.question
    return question

@api.get("/userEmpresa/{int:id}",response = EmpresaSchema)
def userEmpresaGet(request,id):
    user = User.objects.filter(pk=id).first() # [0]
    empresa = user.empresa
    return empresa

@api.get("/empresaUser/{int:id}",response = list[UserSchema])
def empresaUserGet(request,id):
    empresa = Empresa.objects.filter(pk=id).first() # [0]
    users = empresa.user_set
    return users

@api.delete("/deleteUser/{int:id}",response = UserSchema)
def deleteUser(request,id):
    user = User.objects.filter(pk=id).first()
    User.objects.filter(pk=id).first().delete()
    return user

@api.patch("/usernameChange/{int:id}/{str:username}",response = UserSchema)
def usernameChange(request, id, username):
    user = User.objects.filter(pk=id).first()
    user.username = username
    return user

@api.put("/replaceWithAnotherUser/{int:id}/{int:toReplace}",response = UserSchema)
def replaceWithAnotherUser(request, id, toReplace):
    user = User.objects.filter(pk=id).first()
    user.pk = toReplace
    user.username = 'null'
    #user2 = User.objects.filter(pk=toReplace).first()
    user.save()
    return user

@api.post("/createUser/{str:username}/{str:password}",response = UserSchema)
def createUser(request, username, password):
    user = User()
    user.username = username
    user.password = password
    user.save()
    return user



urlpatterns = [
    path("api/", api.urls),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
