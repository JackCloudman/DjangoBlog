# Generated by Django 2.0.8 on 2018-08-21 04:15

import apps.blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='foto_encabezado',
            field=models.ImageField(blank=True, null=True, upload_to=apps.blog.models.update_filename),
        ),
    ]