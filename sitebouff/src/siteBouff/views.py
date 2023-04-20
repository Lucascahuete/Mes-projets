from django.shortcuts import render


def acceuil(request):
    return render(request, "Accueil.html")
