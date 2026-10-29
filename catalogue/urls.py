from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_livres, name='liste_livres'),
    path('ajouter/', views.ajouter_livre, name='ajouter_livre'),
    path('<int:livre_id>/modifier/', views.modifier_livre, name='modifier_livre'),
]