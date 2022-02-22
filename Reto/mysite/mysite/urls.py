
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

@api.get("/user/{int:id}",response = UserSchema)
def userGet(request,id):
    user = User.objects.filter(pk=id).first() # [0]
    return user

@api.get("/users",response = List[UserSchema])
def usersGet(request):
    users = User.objects.all()
    return list(users)

urlpatterns = [
    path("api/", api.urls),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
