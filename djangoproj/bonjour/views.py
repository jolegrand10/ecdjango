from django.shortcuts import render

# Create your views here.


def index(request):
    # pour django une vue est une fonction
    # qui reçoit une requete http
    # qui renvoit une réponse http
    context = {
        'title':"* B o n j o u r *",
        'content': "Je dis Bonjour ici car voilà"
    }
    return render(request, 'bonjour/index.html', context)