from django.shortcuts import redirect, render
from django.http import HttpResponse
from crud.models import *

# Create your views here.

def root (request):
    return redirect('/home')

def home (request):
    return render (request,'core/home.html')

def productos(request):
    context = {'productos':Producto.objects.all()}
    return render(request,'core/productos.html',context)

def locales (request):
    return render (request,'core/locales.html')

def delivery (request):
    return render (request,'core/delivery.html')
def pago (request):
    return render (request,'core/pago.html')