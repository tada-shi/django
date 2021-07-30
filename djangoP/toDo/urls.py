from django.urls import path
from . import views

urlPatters = [
    path('', views.home),
    path('addToDo', views.addToDo),
    path('delToDo/<int:toDo_id>/', views.delToDo)
]