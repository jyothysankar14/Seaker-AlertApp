from django.contrib import admin
from .models import Metric

class MetricAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'cpu_usage', 'ram_usage', 'disk_space', 'uptime')  # Adjust fields here
    list_filter = ('timestamp',)  # Ensure the fields in list_filter exist in the model

admin.site.register(Metric, MetricAdmin)
