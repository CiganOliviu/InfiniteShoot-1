# Generated by Django 3.0.8 on 2021-01-15 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageclient',
            old_name='product',
            new_name='client',
        ),
    ]