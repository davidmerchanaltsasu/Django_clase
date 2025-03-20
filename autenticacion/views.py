from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from autenticacion.forms import RegisterForm, LoginForm
from autenticacion.models import CustomUser


# Create your views here.
def registrar(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['name']
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'El email ya está registrado.')
                return render(request, 'autenticacion/registro.html', {'form': form})

                user = CustomUser.objects.create_user(name=name, email=email, password=password)
                messages.success(request, 'Usuario creado correctamente.')
                return redirect('login')
            else:
                return render(request, 'autenticacion/registro.html', {'form': form})
        form = RegisterForm()
        return render(request, 'autenticacion/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('listar_empleados')
    else:
        form = LoginForm()
    return render(request, 'autenticacion/login.html', {'form': form})

def logout(request):
    django.contrib.auth.logout(request)
    return redirect('login')