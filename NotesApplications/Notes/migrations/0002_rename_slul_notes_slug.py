# Generated by Django 5.0.4 on 2024-04-29 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='slul',
            new_name='slug',
        ),
    ]