from django.shortcuts import render
from django.http import *
from .models import Product


# Create your views here.

def home(request):
    pagename = 'Home'
    name = 'Your Shop'
    return render(request,
                  context={'pagename':pagename,'name':name},
                  template_name='nav.html' )

def contact(request):
    pagename = 'Contact Us'
    name = 'Your Shop'
    return render(request,
                  context={'pagename':pagename,'name':name},

                  template_name='nav.html'
                  )

def products(request):
    pagename = 'Products'
    name = 'Your Shop'
    prods = Product.objects.all()
    return render(request,
                  context={'pagename':pagename,'name':name,'prods':prods},

                  template_name='products.html'
                  )
