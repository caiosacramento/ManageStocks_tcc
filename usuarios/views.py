from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy
# Create your views here.

class usuarioCreate(CreateView):
    template_name = 'usuarios/form-cadastro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')