from django.contrib import admin
from .models import Document, Emprunt,Abonne

admin.site.register(Document)
admin.site.register(Emprunt)
admin.site.register(Abonne)