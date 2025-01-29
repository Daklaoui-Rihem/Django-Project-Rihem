# Generated by Django 5.1.4 on 2025-01-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_subscription_purchased_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='purchased_plan',
            field=models.CharField(choices=[('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Platinium', 'Platinium'), ('Gold', 'Gold')], default='Bronze', max_length=50),
        ),
    ]
