# Importar o TemplateView para criar páginas simples
from django.views.generic import TemplateView


# Create your views here.

# A classe PaginaInicial "extends" TemplateView
class PaginaInicial(TemplateView):
    # Toda classe filha do TemplateView precisa do
    # atributo abaixo para definir um template a ser renderizado
    template_name = 'principal/index.html'
 
class SobreView(TemplateView):
    template_name = 'principal/sobre.html'

class UsarView(TemplateView):
    template_name = 'principal/usar.html'