from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('addexp',views.addexpense),
    path('display',views.displayexpense),
    path('display2',views.displaybalance),
    path('credit',views.creditcash),
]