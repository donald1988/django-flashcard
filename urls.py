from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.home, name = "home"),
    path('index/add.html', views.add, name = "add"),
    path('index/subtract.html/', views.subtract, name = "subtract"),
    path('index/multiply.html/', views.multiply, name = "multiply"),
    path('index/divide.html/', views.divide, name = "divide"),
]
