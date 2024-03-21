from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.CreateUserAPI.as_view()),
    path('login/', views.UserLoginAPI.as_view()),
    path('edit-user/', views.UserEditApi.as_view()),
    path('suggest/', views.UserSuggestionAPI.as_view())
]
