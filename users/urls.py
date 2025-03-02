from django.urls import path
from .views import *

urlpatterns =[
    path('login/',login),
    path('signup/',signup),
    path('logout/',logout),
]