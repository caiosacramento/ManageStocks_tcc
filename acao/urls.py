from django.urls import path
from . import views
from .views import CarteiraCreate
from .views import CarteiraDelete
from .views import CarteiraLista
from .views import CarteiraUpdate
urlpatterns = [
    path('wallet/register', CarteiraCreate.as_view(), name='wallet'),
    path('wallet/delete/<int:pk>', CarteiraDelete.as_view(), name='wallet-delete'),
    path('wallet/lista/', CarteiraLista.as_view(), name='wallet-lista'),
    path('wallet/edita/<int:pk>', CarteiraUpdate.as_view(), name='wallet-edita'),
]