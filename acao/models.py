from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Contato
from django.core.mail import send_mail
# Create your models here.


class Acao(models.Model): #acao da bolsa, preço atualizado diariamente
    nome = models.CharField(max_length=10)
    valor_atual = models.IntegerField(verbose_name="valor atual")


    def __str__(self):
        return "{} ({})".format(self.nome, self.valor_atual)

class CarteiraAcao(models.Model) : #acao cliente, preço historico comparado com o preço atual
    acao = models.ForeignKey(Acao, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    valor_comprado = models.IntegerField(verbose_name="valor comprado",default=0)
    data = models.DateField()  
    variacao_calculada = models.FloatField(verbose_name="variação", blank=True, null=True)
    variacao_limite = models.FloatField(verbose_name="variação", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.variacao_calculada = self.acao.valor_atual / self.valor_comprado 
        super().save(*args, **kwargs)

    def envia_email(self):
        subject = 'Welcome!'
        message = f'Hello {self.usuario.first_name}, welcome to our website!'
        from_email = 'your@example.com'
        recipient_list = [self.usuario.email]
        send_mail(subject, message, from_email, recipient_list)

    def variacao_calculada_funcao(self):
        return self.variacao_calculada
    #campo calculado diferenca = models.IntegerField(valor_atual) - models.IntegerField(valor_comprado)

    #def mandar_email(self, User):
        #if self.variacao_calculada >= self.variacao_limite:
            #send_mail('assunto','a ação {self.acao} ta tendo uma variação','icmercadoacao@gmail.com',['{User.email}'])
    #@property
    #def variacao(self):
        #return round(self.valor_comprado / self.acao.valor_atual, 2)
    
    def __str__(self):
        return "{} ({})".format(self.acao.nome,self.valor_comprado,self.acao.valor_atual)