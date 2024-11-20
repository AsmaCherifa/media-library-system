from djongo import models

class Emprunt(models.Model):
    abonne = models.ForeignKey('Abonne', on_delete=models.CASCADE)
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    date_emprunt = models.DateField()
    date_retour_prevue = models.DateField()
    statut_emprunt = models.CharField(max_length=50, choices=[('En cours', 'En cours'), ('Terminé', 'Terminé')])

    def __str__(self):
        return f"Emprunt de {self.abonne} pour {self.document}"

class Abonne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Document(models.Model):
    titre = models.CharField(max_length=200)
    type = models.CharField(max_length=100) 
    auteur = models.CharField(max_length=100)
    date_publication = models.DateField()
    disponibilite = models.BooleanField(default=True)

    def __str__(self):
        return self.titre
