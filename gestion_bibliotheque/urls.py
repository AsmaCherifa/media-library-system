# gestion_bibliotheque/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from bibliotheque.test_prometheus import metrics_view  # Assurez-vous que cet import est correct

router = DefaultRouter()

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include('bibliotheque.urls')),
path('metrics/', metrics_view, name='prometheus_metrics'),
#path('test-metrics/', test_metrics, name='test_metrics'),

]
