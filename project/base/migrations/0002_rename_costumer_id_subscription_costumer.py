# Generated by Django 5.1.4 on 2025-01-24 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='costumer_id',
            new_name='costumer',
        ),
    ]
