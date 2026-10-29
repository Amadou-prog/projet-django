from django.shortcuts import render, redirect
from .forms import LivreForm
# Create your views here.
from .models import Livre
def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'catalogue/liste.html', {'livres': livres})



def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'catalogue/ajouter.html', {'form': form})