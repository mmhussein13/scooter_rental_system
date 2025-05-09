# Generated by Django 5.2 on 2025-05-08 19:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_purchaseitem_store'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(choices=[('low_stock', 'Low Stock'), ('overdue_rental', 'Overdue Rental'), ('maintenance_due', 'Maintenance Due'), ('expiring_item', 'Expiring Item'), ('price_change', 'Price Change')], max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('severity', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('critical', 'Critical')], default='medium', max_length=10)),
                ('status', models.CharField(choices=[('new', 'New'), ('acknowledged', 'Acknowledged'), ('resolved', 'Resolved'), ('dismissed', 'Dismissed')], default='new', max_length=15)),
                ('threshold_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('current_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('email_sent', models.BooleanField(default=False)),
                ('dashboard_notification', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_acknowledged', models.DateTimeField(blank=True, null=True)),
                ('date_resolved', models.DateTimeField(blank=True, null=True)),
                ('acknowledged_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='acknowledged_alerts', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_alerts', to=settings.AUTH_USER_MODEL)),
                ('part', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='inventory.parts')),
                ('resolved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resolved_alerts', to=settings.AUTH_USER_MODEL)),
                ('scooter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='inventory.scooter')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='inventory.store')),
            ],
            options={
                'ordering': ['-severity', '-date_created'],
            },
        ),
    ]
