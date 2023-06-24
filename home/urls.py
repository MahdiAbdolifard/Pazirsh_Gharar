from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='allstudent'),
    path('create/', views.create, name='create'),
]