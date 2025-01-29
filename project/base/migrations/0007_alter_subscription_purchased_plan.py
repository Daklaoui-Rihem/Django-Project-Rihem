# Generated by Django 5.1.4 on 2025-01-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_subscription_purchased_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='purchased_plan',
            field=models.CharField(choices=[('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Platinum', 'Platinum'), ('Gold', 'Gold')], default='Bronze', max_length=50),
        ),
    ]
