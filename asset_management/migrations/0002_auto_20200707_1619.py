# Generated by Django 3.0.8 on 2020-07-07 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
