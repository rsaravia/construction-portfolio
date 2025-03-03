from django.shortcuts import render
from .models import Projects

# Create your views here.
def home(request):
    items = Projects.objects.all()
    return render(request, 'home_app/home.html',
                  {'items':items})