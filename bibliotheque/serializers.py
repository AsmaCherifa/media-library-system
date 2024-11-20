from rest_framework import serializers
from .models import Abonne, Document, Emprunt

class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = '__all__'

class AbonneSerializer(serializers.ModelSerializer):
    liste_emprunts = EmpruntSerializer(many=True, read_only=True, source='emprunt_set')  # Utilise la relation inversée
    historique_emprunts = EmpruntSerializer(many=True, read_only=True, source='emprunt_set')  # À ajuster selon logique

    class Meta:
        model = Abonne
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
