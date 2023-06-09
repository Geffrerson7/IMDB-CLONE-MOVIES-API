# Generated by Django 4.2.1 on 2023-06-01 17:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='production_companies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None),
        ),
    ]
