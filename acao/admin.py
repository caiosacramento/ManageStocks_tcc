from django.contrib import admin

# Register your models here.

from .models import Acao, CarteiraAcao


admin.site.register(Acao)
admin.site.register(CarteiraAcao)