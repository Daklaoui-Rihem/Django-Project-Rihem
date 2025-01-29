import stripe
import json
from decouple import config

# Set your Stripe API key
stripe.api_key = config('STRIPE_SECRET_KEY')

# Define your item list
item_list = {
    "Bronze": {
        "description": "3 apps for 12 months",
        "amount": 10000,
        "currency": "usd"
    },
    "Silver": {
        "description": "9 apps for 12 months",
        "amount": 25000,
        "currency": "usd"
    },
    "Gold": {
        "description": "12 apps for 12 months",
        "amount": 50000,
        "currency": "usd"
    },
    "Platinum": {
        "description": "15 apps for 12 months",
        "amount": 75000,
        "currency": "usd"
    }
}

# Create a checkout session
def create_checkout_session(items):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                "price_data": {
                    "currency": item["currency"],
                    "product_data": {
                        "name": key,
                        "description": item["description"]
                    },
                    "unit_amount": item["amount"]
                },
                "quantity": 1
            }
            for key, item in items.items()
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/success',
        cancel_url='http://127.0.0.1:8000/cancel',
    )
    return session.url

# Example usage
if __name__ == "__main__":
    payment_url = create_checkout_session(item_list)
    print("Payment URL:", payment_url)
