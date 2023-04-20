import botbouff
import random
from django.shortcuts import render

from .models import Author
# Create your views here.


def qui(request):
    for i, j in botbouff.messages.items():
        if i not in Author.objects.values_list('pseudo', flat=True):
            author = Author(pseudo=i, content=j)
            author.save()
        else:
            data = Author.objects.get(pseudo=i)
            data.content = j
            data.save()
    #choisir un auteur aleatoire
    a = Author.objects.all()
    choix_pseudo = random.choice(a)
    bonne_reponse = choix_pseudo.pseudo.format()
    #choisir un message alleatoir de cette auteur
    b = Author.objects.get(pseudo=bonne_reponse)
    liste_brut = b.content
    liste_brut = liste_brut.replace("[","").replace("]","").format()
    liste = liste_brut.split(", ")
    choix_message = random.choice(liste)
    question = choix_message.format()
    #Faire une liste des 4choix avec l'auteur et trois autre auteur aleatoire
    reponse = [bonne_reponse]
    lst_pseudo = []
    for i in Author.objects.all():
        a = i.pseudo.format()
        lst_pseudo.append(a)
    lst_pseudo.remove(bonne_reponse)
    autre_reponse = random.choices(lst_pseudo, k=3)
    for i in autre_reponse:
        reponse.append(i)
    #renvoyern le message et les auteur dans la vue
    return render(request, "qui-a-dit-ca.html", {"question": question,
                                                 "reponse1": reponse[0],
                                                 "reponse2": reponse[1],
                                                 "reponse3": reponse[2],
                                                 "reponse4": reponse[3]})
