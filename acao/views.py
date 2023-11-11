from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import CarteiraAcao
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404
#create your views here
##################CREATE##################
class CarteiraCreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = CarteiraAcao
    template_name = 'acao/form.html'
    fields = ['acao','qtd_acao','valor_comprado', 'variacao_limite' , 'data']
    success_url = reverse_lazy('wallet-lista')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        #antes do super o objeto ainda não foi criado
        url = super().form_valid(form)
        return url


##################UPDATE##################
class CarteiraUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = CarteiraAcao
    fields = ['acao','qtd_acao','valor_comprado','variacao_limite','data']
    template_name = 'acao/form.html'
    success_url = reverse_lazy('wallet-lista')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(CarteiraAcao, pk=self.kwargs['pk'],usuario=self.request.user)
        return self.object

##################DELETE##################
class CarteiraDelete(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = CarteiraAcao
    template_name = 'acao/form-delete.html'
    success_url = reverse_lazy('wallet-lista')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(CarteiraAcao, pk=self.kwargs['pk'],usuario=self.request.user)
        return self.object
##################LIST##################

class CarteiraLista(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = CarteiraAcao
    template_name = 'acao/lista/dashboard.html'
    paginate_by = 5
    
    def send_email(self,recipient,subject,body):
        if self.variacao_limite >= CarteiraAcao.variacao_calculada :
            send_mail('teste','teste',None,['{self.request.user.email}'])
    def get_queryset(self):
        self.object_list = CarteiraAcao.objects.filter(usuario = self.request.user)
        return self.object_list