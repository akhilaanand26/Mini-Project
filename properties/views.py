from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'properties/home.html')
def reservation(request):
    return render(request,'properties/reservation.html')
def wishlist(request):
    return render(request,'properties/wishlist.html')
    from django.shortcuts import render, redirect

from .models import Property



def home(request):
    return render(request, 'properties/home.html') 




def property_detail(request, slug):
    return render(request, 'properties')


