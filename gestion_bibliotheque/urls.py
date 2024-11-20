# gestion_bibliotheque/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin

router = DefaultRouter()

urlpatterns = [
   path('admin/', admin.site.urls),
    path('api/', include('bibliotheque.urls')),

]
