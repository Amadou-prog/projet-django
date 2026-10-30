from django.shortcuts import render, redirect , get_object_or_404
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


def modifier_livre(request, livre_id):
    livre = get_object_or_404(Livre, id= livre_id)
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm(instance=livre)
    return render(request, 'catalogue/modifier.html', {'form': form})


def supprimer_livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    if request.method == 'POST':
        livre.delete()
        return redirect('liste_livres')
    return render(request, 'catalogue/supprimer.html', {'livre': livre})