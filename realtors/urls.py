from django.urls import path
from .views import import_realtor_data
from . import views

urlpatterns =[
  path('',import_realtor_data,name='import_realtor_data')
]