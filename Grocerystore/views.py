from django.shortcuts import render
from .models import grocery

# Create your views here.

def index(request):

    gro = grocery.objects.all()
    return render(request, 'index.html', {'gro': gro} ) 
