from rest_framework import serializers
from .models import Emprunt, Abonne, Document
from datetime import date

class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = '__all__'


class AbonneSerializer(serializers.ModelSerializer):
    liste_emprunts = EmpruntSerializer(many=True, read_only=True, source='emprunt_set')
    historique_emprunts = EmpruntSerializer(many=True, read_only=True, source='emprunt_set')  

    class Meta:
        model = Abonne
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
