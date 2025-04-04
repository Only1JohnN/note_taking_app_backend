# Generated by Django 5.1.8 on 2025-04-03 10:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0003_alter_notesmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesmodel',
            name='body',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='notesmodel',
            name='title',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
