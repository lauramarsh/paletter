# Generated by Django 3.1.2 on 2020-10-27 06:59

import be_paletter.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_paletter', '0005_remove_palettes_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='palettes',
            name='colors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=be_paletter.models.list_default, size=None),
        ),
    ]