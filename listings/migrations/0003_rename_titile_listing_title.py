# Generated by Django 3.2.4 on 2021-06-09 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210609_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='titile',
            new_name='title',
        ),
    ]