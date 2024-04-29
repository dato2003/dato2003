from django.urls import path
from . import views

urlpatterns=[
    path("register/",views.RegisterView.as_view(),name="register"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("logaut/",views.LogoutView.as_view(),name="logout"),
    path("note/",views.NoteView.as_view(),name="create//list"),
    path("note/detail/<int:pk>",views.NoteDetailViews.as_view(),name="delete/update/Rtr.")
]