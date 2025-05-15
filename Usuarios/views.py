from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import LoginForm
from .models import Usuario

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            try:
                user = Usuario.objects.get(usuario=usuario, password=password)
                return redirect('dashboard')
            except Usuario.DoesNotExist:
                error_message = "Datos invalidos"
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard_view(request):
    return render(request, 'dashboard.html')