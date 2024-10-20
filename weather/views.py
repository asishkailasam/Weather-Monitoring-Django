from django.shortcuts import render
from .models import WeatherData, DailySummary
from .forms import AlertThresholdForm

def weather_summary(request):
    summaries = DailySummary.objects.all()
    return render(request, 'weather_summary.html', {'summaries': summaries})

def set_alert(request):
    if request.method == 'POST':
        form = AlertThresholdForm(request.POST)
        if form.is_valid():
            threshold = form.cleaned_data['temperature_threshold']
            # Add logic for threshold-based alert
    else:
        form = AlertThresholdForm()
    return render(request, 'set_alert.html', {'form': form})
