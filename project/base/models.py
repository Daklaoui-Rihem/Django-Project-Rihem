from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    PLAN_CHOICES = [
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
        ('None', 'None'),
    ]

    PAYMENT_METHODS = [
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
    ]

    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", default=None)
    django_id = models.CharField(max_length=255, unique=True, default='')
    stripe_transaction_id = models.CharField(max_length=255, null=True, blank=True, default='')
    list_of_items = models.JSONField(default=dict)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    datetime = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='Not Specified')
    purchased_plan = models.CharField(max_length=50, choices=PLAN_CHOICES, default='None')

    def __str__(self):
        return f"Order {self.id} for {self.user.username}"

