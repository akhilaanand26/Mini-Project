from django.urls import path
from .views import properties_views



app_name='owner'

urlpatterns = [

    path('',properties_views,name='properties'),
]