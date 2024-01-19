# home/admin.py
from django.contrib import admin
from .models import RiskData  # Import your RiskData model

# Register the RiskData model
admin.site.register(RiskData)
