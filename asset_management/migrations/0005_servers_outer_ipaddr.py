# Generated by Django 3.0.8 on 2020-07-24 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0004_remove_servers_power_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='outer_ipaddr',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
