from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def stock(request):
    if request.method != 'POST':
        return render(request, 'accounts/stock.html')
    
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario,  password=senha)
    if not user:
        messages.error(request, 'usuario ou senha inválidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'logado com sucesso')
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('dashboard')

def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio')
        return render(request, 'accounts/register.html')
    try:
        validate_email(email)
    except:
        messages.error(request, 'email invalido ')
        return render(request, 'accounts/register.html')
    if len(senha) < 6:
        messages.error(request, 'senha precisa 8 caracteres ou mais ')
        return render(request, 'accounts/register.html')
    if len(usuario) < 4:
        messages.error(request, 'usuario precisa 4 caracteres ou mais ')
        return render(request, 'accounts/register.html')
    if senha != senha2:
        messages.error(request, 'Senhas diferentes ')
        return render(request, 'accounts/register.html')
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'usuario já cadastrado ')
        return render(request, 'accounts/register.html')
    if User.objects.filter(email=email).exists():
        messages.error(request, 'email já cadastrado ')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Usuario cadastrado com sucesso')
    user = User.objects.create_user(username=usuario,
                                    email=email,
                                    password=senha,
                                    first_name=nome,
                                    last_name=sobrenome)
    user.save()
    return redirect('login')



@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


