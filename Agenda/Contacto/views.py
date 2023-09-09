from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .models import Contacto
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'inicio.html')
        else:
            pass
    return render(request, 'login.html')

def INICIO(request):
    return render(request,'inicio.html')

def contacto(request):
    contactos = Contacto.objects.all()
    context = {"contactos":contactos}
    return render(request, 'contactos.html', context)

def buscar_contacto(request):
    if request.method == 'GET':
        nombre = request.GET.get('txtnombre')
        contactos = Contacto.objects.filter(nombre__icontains=nombre)
        return render(request, 'contactos.html', {'contactos': contactos})
    
def eliminarcontacto(request, codigo):
    contacto=Contacto.objects.get(codigo=codigo)
    contacto.delete()
    contactos = Contacto.objects.order_by('codigo')
    return render(request, 'contactos.html', {"contactos":contactos})

def registrarcontacto(request):
    nombre = request.POST["txtnombre"]
    numero = request.POST["txtnumero"]
    email = request.POST["txtemail"]

    contacto=Contacto.objects.create(nombre=nombre,numero=numero, email = email)
    contacto.save()
    contactos = Contacto.objects.order_by('codigo')
    return render(request, 'contactos.html', {"contactos":contactos})

def editarcontacto(request, codigo):
    nombre = request.POST["txtnombre"]
    numero = request.POST["txtnumero"]
    email = request.POST["txtemail"]

    contacto = Contacto.objects.get(codigo=codigo)
    contacto.nombre = nombre
    contacto.numero = numero
    contacto.email = email
    contacto.save()
    return redirect("/contactos")
