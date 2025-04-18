# Generated by Django 5.1.8 on 2025-04-18 15:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0005_alter_notesmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='notesmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notesmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
