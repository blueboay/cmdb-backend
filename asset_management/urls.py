
from django.urls import path
from . import ecs
from . import rds

urlpatterns = [
    path('ecs', ecs.listServers),
    path('rds', rds.listRDS)
]
