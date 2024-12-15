# Generated by Django 5.1.4 on 2024-12-15 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metric',
            old_name='device_uptime',
            new_name='disk_space',
        ),
        migrations.RenameField(
            model_name='metric',
            old_name='disk_usage',
            new_name='uptime',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='cpu_temperature',
        ),
    ]