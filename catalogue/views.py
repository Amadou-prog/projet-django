from django.shortcuts import render

# Create your views here.
from .models import Livre
def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'catalogue/liste.html', {'livres': livres})