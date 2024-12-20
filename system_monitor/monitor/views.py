from django.shortcuts import render
from .models import Metric

def dashboard(request):
    """
    Display the latest system metrics and historical data.
    """
    # Fetch the latest system metrics
    latest_metric = Metric.objects.order_by('-timestamp').first()

    # Fetch historical metrics (last 10 records)
    historical_metrics = Metric.objects.order_by('-timestamp')[:10]

    context = {
        'latest_metric': latest_metric,
        'historical_metrics': historical_metrics,
    }
    return render(request, 'monitor/dashboard.html', context)
