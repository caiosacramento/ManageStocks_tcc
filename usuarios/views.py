from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from .forms import UsuarioForm, UsuarioUpdateForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
# Create your views here.

class usuarioCreate(CreateView):
    template_name = 'usuarios/form-cadastro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')



##################UPDATE##################
class userUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    form_class = UsuarioUpdateForm
    template_name = 'usuarios/form-update.html'
    success_url = reverse_lazy('wallet-lista')

    def form_valid(self, form):
        user = form.save(commit=True)
        user.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_object(self, queryset=None):
        self.object = get_object_or_404(User,username=self.request.user)
        return self.object