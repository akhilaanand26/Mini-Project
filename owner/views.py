from django.shortcuts import render


# Create your views here.
def properties_views(request):
   return render(request,'owner/properties.html')

