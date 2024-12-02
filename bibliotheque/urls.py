from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),

    path('abonnes/', views.abonne_list, name='abonne_list'),
    path('abonnes/create/', views.abonne_create, name='abonne_create'),
    path('abonnes/<int:pk>/update/', views.abonne_update, name='abonne_update'),
    path('abonnes/<int:pk>/delete/', views.abonne_delete, name='abonne_delete'),
    
    path('documents/', views.document_list, name='document_list'),
    path('documents/create/', views.document_create, name='document_create'),
    path('documents/<int:pk>/update/', views.document_update, name='document_update'),
    path('documents/<int:pk>/delete/', views.document_delete, name='document_delete'),
    
    path('emprunts/', views.emprunt_list, name='emprunt_list'),
    path('emprunts/create/', views.emprunt_create, name='emprunt_create'),
    path('emprunts/<int:pk>/update/', views.emprunt_update, name='emprunt_update'),
    path('emprunts/<int:pk>/delete/', views.emprunt_delete, name='emprunt_delete'),

    path('tableau-de-bord/', views.tableau_de_bord, name='tableau_de_bord'),

    path('chercher_abonne/', views.chercher_abonne, name='chercher_abonne'),
    path('chercher_document/', views.chercher_document, name='chercher_document'),
    path('chercher_emprunt/', views.chercher_emprunt, name='chercher_emprunt'),


]
