from django.urls import path
from .views import home
from .views import wishlist
from .views import reservation

app_name='properties'

urlpatterns = [
    path('',home,name='home'),
    path('wishlist/',wishlist,name='wishlist'),
    path('reservation/',reservation,name='reservations'),
]