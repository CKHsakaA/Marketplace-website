from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from item.models import *
from .forms import *

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    
    return render(request, "core/index.html",{
        "items":items,
        "categories":categories
    })


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid:
          form.save()

          return redirect('/login/')
        
    else:    
        form = SignUpForm

    return render(request, "core/signup.html",{
        "form":form
    }) 

def logout_view(request):
    logout(request)
    return redirect('/login/') 
 

