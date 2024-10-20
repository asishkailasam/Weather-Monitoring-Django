from django import forms

class AlertThresholdForm(forms.Form):
    temperature_threshold = forms.FloatField(label="Temperature Threshold (°C)")
