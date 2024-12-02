from django_prometheus.exports import ExportToDjangoView
from prometheus_client import Gauge
from .models import Emprunt

loan_terminated_total = Gauge('loan_terminated_total', 'Total number of loans that are terminated')
loan_progress_total = Gauge('loan_progress_total', 'Total number of loans that are in progress')
loan_total = Gauge('loan_total', 'Total number of loans')

def update_loan_metrics():
    terminated_loans = Emprunt.objects.filter(statut_emprunt='Terminé').count()
    loan_terminated_total.set(terminated_loans)  

    progress_loans = Emprunt.objects.filter(statut_emprunt='En cours').count()
    loan_progress_total.set(progress_loans)  

    total_loans = Emprunt.objects.count()  # Récupérer le nombre total d'emprunts
    loan_total.set(total_loans)  

def metrics_view(request):
    update_loan_metrics() 
    return ExportToDjangoView(request)

def test_metrics(request):
    return ExportToDjangoView(request)
