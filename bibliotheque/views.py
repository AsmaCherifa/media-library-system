from django.shortcuts import render, get_object_or_404, redirect
from .models import Abonne, Document, Emprunt
from .forms import AbonneForm, DocumentForm, EmpruntForm
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "asma" and password == "asma":
            return redirect('abonne_list')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

def abonne_list(request):
    abonnes = Abonne.objects.all()  # Get all abonnés
    return render(request, 'abonnes/abonne_list.html', {'abonnes': abonnes})


def abonne_create(request):
    if request.method == 'POST':
        form = AbonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('abonne_list')
    else:
        form = AbonneForm()
    return render(request, 'abonnes/create.html', {'form': form})

def abonne_update(request, pk):
    abonne = get_object_or_404(Abonne, pk=pk)
    if request.method == 'POST':
        form = AbonneForm(request.POST, instance=abonne)
        if form.is_valid():
            form.save()
            return redirect('abonne_list')
    else:
        form = AbonneForm(instance=abonne)
    return render(request, 'abonnes/update.html', {'form': form})

def abonne_delete(request, pk):
    abonne = get_object_or_404(Abonne, pk=pk)
    if request.method == 'POST':
        abonne.delete()
        return redirect('abonne_list')
    return render(request, 'abonnes/delete.html', {'abonne': abonne})

def chercher_abonne(request):
    query = request.GET.get('q')  # Récupérer le mot-clé depuis les paramètres GET
    if query:
        abonnes = Abonne.objects.filter(
            Q(nom__icontains=query) |
            Q(prenom__icontains=query) |
            Q(adresse__icontains=query) |
            Q(date_inscription__icontains=query)  # Recherche par date
        )
    else:
        abonnes = Abonne.objects.all()
    return render(request, 'abonnes/abonne_list.html', {'abonnes': abonnes})


# Document Views
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents/document_list.html', {'documents': documents})

def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'documents/document_create.html', {'form': form})

def document_update(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'documents/document_update.html', {'form': form})

def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'documents/document_delete.html', {'document': document})

def chercher_document(request):
    query = request.GET.get('q')
    if query:
        documents = Document.objects.filter(
            Q(titre__icontains=query) |
            Q(auteur__icontains=query) |
            Q(type__icontains=query)
        )
    else:
        documents = Document.objects.all()
    
    # Add a message if no documents are found
    message = None
    if query and not documents.exists():
        message = "No results found."
    
    return render(request, 'documents/document_list.html', {
        'documents': documents,
        'query': query,
        'message': message,
    })


# Emprunt Views
def emprunt_list(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'emprunts/emprunt_list.html', {'emprunts': emprunts})

def emprunt_create(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emprunt_list')
    else:
        form = EmpruntForm()
    return render(request, 'emprunts/emprunt_create.html', {'form': form})



def emprunt_update(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    if request.method == 'POST':
        form = EmpruntForm(request.POST, instance=emprunt)
        if form.is_valid():
            form.save()
            return redirect('emprunt_list')
    else:
        form = EmpruntForm(instance=emprunt)
    return render(request, 'emprunts/emprunt_update.html', {'form': form})

def emprunt_delete(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    if request.method == 'POST':
        emprunt.delete()
        return redirect('emprunt_list')
    return render(request, 'emprunts/emprunt_delete.html', {'emprunt': emprunt})

def chercher_emprunt(request):
    query = request.GET.get('q')  # Récupérer le mot-clé des paramètres GET
    if query:
        # Filtrer les emprunts par plusieurs champs
        emprunts = Emprunt.objects.filter(
            Q(abonne__nom__icontains=query) |  # Recherche par le nom de l'abonné
            Q(abonne__prenom__icontains=query) |  # Recherche par le prénom de l'abonné
            Q(document__titre__icontains=query) |  # Recherche par le titre du document
            Q(statut_emprunt__icontains=query)  # Recherche par statut d'emprunt
        )
    else:
        emprunts = Emprunt.objects.all()  # Si aucun mot-clé, retourner tous les emprunts
    return render(request, 'emprunts/emprunt_list.html', {'emprunts': emprunts})


def tableau_de_bord(request):
    # Statistiques
    total_emprunts = Emprunt.objects.count()
    emprunts_en_cours = Emprunt.objects.filter(statut_emprunt="En cours").count()
    emprunts_termines = Emprunt.objects.filter(statut_emprunt="Terminé").count()

    # Derniers emprunts
    derniers_emprunts = Emprunt.objects.order_by('-date_emprunt')[:5]

    # Context pour le tableau de bord
    context = {
        'total_emprunts': total_emprunts,
        'emprunts_en_cours': emprunts_en_cours,
        'emprunts_termines': emprunts_termines,
        'derniers_emprunts': derniers_emprunts,
    }
    return render(request, 'tableau_de_bord.html', context)


'''api_requests_total = Counter('api_requests_total', 'Total API requests', ['endpoint'])

def example_view(request):
    api_requests_total.labels(endpoint='example_view').inc() 
    return JsonResponse({'message': 'Hello, Prometheus!'})'''