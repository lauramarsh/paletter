# Generated by Django 3.1.2 on 2020-10-27 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('be_paletter', '0004_palettes_colors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palettes',
            name='colors',
        ),
    ]
