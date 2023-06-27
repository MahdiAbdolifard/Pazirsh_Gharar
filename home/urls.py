from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.test, name='allstudent'),
    path('', views.create, name='create'),
    path('group/', views.group, name='group'),
    path('grade/', views.grade, name='grade'),
    path('school/', views.school, name='school'),
    
]
