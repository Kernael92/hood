from django.shortcuts import render,redirect
from .models import Profile,Business,Hood
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    posts = Post.objects.all()
    return render(request,'hood/home.html',{'posts':posts})



