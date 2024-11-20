from django.urls import reverse
from django.test import TestCase
from .models import Abonne, Document,Emprunt

class AbonneModelTest(TestCase):

    def setUp(self):
        self.abonne = Abonne.objects.create(nom="John", prenom="Doe", adresse="123 Street")

    def test_abonne_creation(self):
        abonne = self.abonne
        self.assertEqual(abonne.nom, "John")
        self.assertEqual(abonne.prenom, "Doe")
        self.assertEqual(abonne.adresse, "123 Street")
        self.assertIsNotNone(abonne.date_inscription)


class EmpruntCreateTestCase(TestCase):
    def setUp(self):
        self.abonne = Abonne.objects.create(nom="Test", prenom="User", adresse="Test Adresse")
        self.document = Document.objects.create(titre="Test Document", type="Livre", auteur="Auteur Test", date_publication="2022-01-01")

    def test_creer_emprunt(self):
        data = {
            'abonne': self.abonne.id,
            'document': self.document.id,
            'date_emprunt': '2023-11-20',
            'date_retour_prevue': '2023-11-30',
            'statut_emprunt': 'En cours',
        }
        response = self.client.post(reverse('emprunt_create'), data)
        self.assertEqual(response.status_code, 302)  # Vérifier redirection après création
        self.assertEqual(Emprunt.objects.count(), 1)  # Vérifier qu'un emprunt a été créé
        emprunt = Emprunt.objects.first()
        self.assertEqual(emprunt.statut_emprunt, "En cours")
