
from django.urls import path
from . import views

urlpatterns = [
    path('ecs', views.listServers)
]
