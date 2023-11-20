from django.core.management.base import BaseCommand
from acao.models import Acao, CarteiraAcao
from django.contrib.auth.models import User
import pandas as pd  
from yahoofinancials import YahooFinancials
from datetime import date 
import mysql.connector
from django.core.mail import send_mail
from django.conf import settings

mydb = mysql.connector.connect(
    #host = "localhost",
    host="managestockufbadatabase.mysql.database.azure.com",
    #user = "root",
    user="managestockadm",
    password  = "Caio12345",
    database = "databasemanagestocks",
    auth_plugin='mysql_native_password',
    port=3306
)

dataAtual = date.today()
my_cursor = mydb.cursor()
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        acoes = Acao.objects.all()
        carteiras = CarteiraAcao.objects.all()
        a = []

        for x in acoes:
            nome_acao = x.nome
            a.append(nome_acao)

        for b in a:
            yahoo_financials = YahooFinancials(b)  
            preco_atualizado = yahoo_financials.get_current_price()
            acaoConstrutor = "UPDATE acao_acao SET valor_atual = %s where nome = %s "
            acaoValores = (preco_atualizado, b) 
            my_cursor.execute(acaoConstrutor,acaoValores)
            mydb.commit() 

        for c in carteiras: #só falta testar se o commit, após isso é só fazer a função de enviar o email
            id = c.id
            nova_variacao = ((c.acao.valor_atual - c.valor_comprado)/ c.valor_comprado) * 100
            variacaoConstrutor = "UPDATE acao_carteiraacao SET variacao_calculada = %s where id = %s "
            variacaoValores = (nova_variacao, id)
            my_cursor.execute(variacaoConstrutor,variacaoValores)
            mydb.commit() 
            montante_antigo = c.valor_comprado * c.qtd_acao
            montante_atual = c.acao.valor_atual * c.qtd_acao
            montante_total = montante_atual - montante_antigo 
            if c.variacao_calculada >= c.variacao_limite:
                if c.valor_comprado >= c.acao.valor_atual:
                    # ação desvalorizando
                    # envia email 
                    lista_email = []
                    lista_email.append(c.usuario.email)
                    subject = f'Atenção para desvalorização da sua ação {c.acao.nome}'
                    message = f'Olá, {c.usuario.first_name}. Sua ação {c.acao.nome} comprada a U${c.valor_comprado} está sendo vendida a U${c.acao.valor_atual} a teve uma desvalorização de {nova_variacao}%, com essa desvalorização você perdeu U${montante_total}'  
                    from_email = settings.DEFAULT_FROM_EMAIL
                    recipient_list = lista_email
                    send_mail(subject, message, from_email, recipient_list)
                    
                elif c.valor_comprado <= c.acao.valor_atual:
                    lista_email = []
                    lista_email.append(c.usuario.email)
                    subject = f'Atenção para valorização da sua ação {c.acao.nome}'
                    message = f'Olá, {c.usuario.first_name}. Sua ação {c.acao.nome} comprada a U${c.valor_comprado} está sendo vendida a U${c.acao.valor_atual} a teve uma valorização de {nova_variacao}%, com essa valorização você ganhou U${montante_total} '
                    from_email = settings.DEFAULT_FROM_EMAIL
                    recipient_list = lista_email
                    send_mail(subject, message, from_email, recipient_list)
