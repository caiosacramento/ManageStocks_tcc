from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='alogin'),
    path('logout/', views.logout, name='alogout'),
    path('register/', views.register, name='aregister'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('stock/', views.stock, name='stock'),
]