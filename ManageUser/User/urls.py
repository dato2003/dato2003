from django.urls import path
from . import views

urlpatterns =[

    path("",views.list_users,name="user list"),
    path("create/",views.create_users,name="create users"),
]