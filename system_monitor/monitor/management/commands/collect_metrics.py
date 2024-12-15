from django.core.management.base import BaseCommand
from monitor .models import Metric
import psutil
import shutil
from datetime import datetime


class Command(BaseCommand):
    help = "Collect system metrics and store them in the database"

    def handle(self, *args, **kwargs):
        # Fetch metrics
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        ram_usage = memory_info.used / (1024 ** 3)  # Convert to GB
        total, used, free = shutil.disk_usage('C:\\')  # Replace with '/' for Linux
        disk_usage = used / (1024 ** 3)  # Convert to GB
        uptime = psutil.boot_time()
        current_time = datetime.now().timestamp()
        device_uptime = (current_time - uptime) / 3600  # Convert to hours

        # Fetch temperature if available
        cpu_temperature = None
        if hasattr(psutil, 'sensors_temperatures'):
            temps = psutil.sensors_temperatures()
            if temps:
                cpu_temp = temps.get('coretemp', [])
                if cpu_temp:
                    cpu_temperature = cpu_temp[0].current

        # Save metrics to database
        Metric.objects.create(
            cpu_usage=cpu_usage,
            ram_usage=ram_usage,
            disk_usage=disk_usage,
            device_uptime=device_uptime,
            cpu_temperature=cpu_temperature,
        )

        self.stdout.write("Metrics collected and stored in the database.")
