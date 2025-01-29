# Generated by Django 5.1.4 on 2025-01-25 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_subscription_purchased_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='purchased_plan',
            field=models.CharField(choices=[('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], default='Bronze', max_length=50),
        ),
    ]
