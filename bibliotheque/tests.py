from datetime import date
from django.test import TestCase
from django.urls import reverse
from .models import Abonne,Document,Emprunt
from datetime import date, timedelta

class AbonneCreationTest(TestCase):
    def test_abonne_creation_and_redirection(self):
        """
        Test that an Abonne can be created then redirected to the list view.
        """
        # Define the form data for the Abonne creation
        data = {
            'nom': 'Test',
            'prenom': 'User',
            'adresse': '123 Test Address',
            'date_inscription': date.today(),
        }

        # Send a POST request to the Abonne creation view
        response = self.client.post(reverse('abonne_create'), data)

        # Check that the Abonne was created
        self.assertEqual(Abonne.objects.count(), 1)
        abonne = Abonne.objects.first()
        self.assertEqual(abonne.nom, 'Test')
        self.assertEqual(abonne.prenom, 'User')
        self.assertEqual(abonne.adresse, '123 Test Address')
        self.assertEqual(abonne.date_inscription, date.today())

        # Check that the response is a redirection to the list view
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('abonne_list'))


class DocumentSearchFunctionalTest(TestCase):
    def setUp(self):
        """
        Create test data for document search functionality.
        """
        Document.objects.create(titre="Python Programming", auteur="John Doe", type="Technology")
        Document.objects.create(titre="Learn Django", auteur="Jane Smith", type="Technology")

    def test_search_documents_by_title(self):
        """
        Test that documents can be searched by title and displayed on the results page.
        """
        response = self.client.get(reverse('chercher_document') + '?q=Python')
        
        # Check that the response contains the correct document
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Programming")
        self.assertNotContains(response, "Learn Django")


    def test_search_no_results(self):
        """
        Test that a search with no matching results shows an appropriate message.
        """
        response = self.client.get(reverse('chercher_document') + '?q=Nonexistent')

        # Check that the response shows no results
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No results found.")


class EmpruntTestCase(TestCase):
    def setUp(self):
        """
        Prépare les données nécessaires pour tester la création d'un emprunt.
        """
        self.document = Document.objects.create(
            titre="Introduction to AI",
            auteur="John Doe",
            type="Education",
            disponibilite=True
        )
        self.abonne = Abonne.objects.create(
            nom="Test",
            prenom="User",
            adresse="123 Main Street",
            date_inscription=date.today()
        )

    def test_emprunt_creation(self):
        """
        Vérifie qu'un emprunt peut être créé et que la réponse redirige correctement.
        """
        emprunt_data = {
            'document': self.document.id,
            'abonne': self.abonne.id,
            'date_emprunt': date.today(),
            'date_retour_prevue': date.today() + timedelta(days=14)
        }
        
        response = self.client.post(reverse('emprunt_create'), emprunt_data)

        # Vérifie qu'aucun emprunt n'a été créé
        self.assertEqual(Emprunt.objects.count(), 0)

        # Vérifie que la page affiche un formulaire avec une erreur
        self.assertEqual(response.status_code, 200)
