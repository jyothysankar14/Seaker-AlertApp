from django.db import models

class Metric(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically sets when the record is created
    cpu_usage = models.FloatField()
    ram_usage = models.FloatField()
    disk_space = models.FloatField()
    uptime = models.FloatField()

    def __str__(self):
        return f"Metrics at {self.timestamp}"
