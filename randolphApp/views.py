from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Jeux, Genre


def index(request):
    return HttpResponse("Bienvenue au Randolph.")

def jeux(request):
    liste_jeux = Jeux.objects.order_by('name')
    context = {
        'liste_jeux': liste_jeux,
    }
    return render(request, 'randolphApp/jeux.html', context)

def detail(request, name_id):
    jeu = get_object_or_404(Jeux, pk=name_id)
    return render(request, 'randolphApp/detailJeu.html', {'jeu': jeu})
