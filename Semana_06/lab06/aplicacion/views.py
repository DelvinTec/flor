from django.shortcuts import render

# Create your views here.
from .models import Producto

def index(request):
    product_list=Producto.objects.order_by('nombre')
    context={'product_list': product_list}
    return render(request, 'index.html', context)



def producto(request):
    return render(request, 'producto.html')

def videojuego(request):
    product_list=Producto.objects.order_by('nombre')
    context={'product_list': product_list}
    return render(request, 'videojuego.html', context)

def rece(request):
    product_list=Producto.objects.order_by('nombre')
    context={'product_list': product_list}
    return render(request, 'rece.html', context)

def consola(request):
    product_list=Producto.objects.order_by('nombre')
    context={'product_list': product_list}
    return render(request, 'consola.html', context)

def maquina(request):
    product_list=Producto.objects.order_by('nombre')
    context={'product_list': product_list}
    return render(request, 'maquina.html', context)


