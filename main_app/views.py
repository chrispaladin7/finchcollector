from django.shortcuts import render
from .models import Finch


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request,'finches/index.html',{
        'finches': finches
    })
