from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.CreateUserAPI.as_view())
]
