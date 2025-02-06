# Generated by Django 5.1.4 on 2025-02-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_subscription_purchased_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='purchased_plan',
            field=models.CharField(choices=[('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum'), ('None', 'None')], default='None', max_length=50),
        ),
    ]
