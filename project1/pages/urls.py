from django.contrib import admin
from django.urls import path, include
from .views import sample,sample2,sample3,sample4,sample5,sample6,sample7,sample8,registration,sample9,sample10,onsubmit,sample11

urlpatterns = [
    path('', sample, name="sample"),
    path('routing/<name>',sample2, name='dr'),
    path('template1',sample3, name='tr'),
    path('passcon', sample4, name="cp"),
    path('lstren', sample5, name='lr'),
    path('redirect', sample6, name="red"),
    path('templateinh', sample7, name='ti'),
    path('staticimage', sample8, name='si'),
    path("register", registration, name='reg'),
    path('formexample', sample9, name='fe'),
    path('datahandling', sample10, name='dh'),
    path('SUBMIT', onsubmit, name='SUBMIT'),
    path('djangoform', sample11, name='df')
]