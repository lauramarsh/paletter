# Generated by Django 3.1.2 on 2020-10-25 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('be_paletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Palette',
            new_name='Palettes',
        ),
        migrations.AlterModelOptions(
            name='palettes',
            options={'ordering': ['name']},
        ),
    ]
