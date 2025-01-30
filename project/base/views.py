from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
import stripe
import json
from django.views.decorators.csrf import csrf_exempt
import uuid
from .models import Subscription
from .forms import UpdateProfileForm

stripe.api_key=settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        user = request.user

        price = stripe.Price.retrieve(product_id)
        product_id_from_price = price.get('product')
        product = stripe.Product.retrieve(product_id_from_price)

        plan_name = product.get('name', 'Unknown Plan')

        plan_price = price['unit_amount'] / 100

        unique_django_id = str(uuid.uuid4())

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': product_id,
                'quantity': 1,
            }],
            mode='subscription',
            billing_address_collection='required',
            success_url='http://127.0.0.1:8000/success',
            cancel_url='http://127.0.0.1:8000/cancel',
        )

        Subscription.objects.create(
            user=user,
            django_id=unique_django_id,
            stripe_transaction_id=session.id,
            list_of_items={"product_id": product_id},
            status='Pending',
            cost=plan_price,
            purchased_plan=plan_name,
            payment='Credit Card',
        )

        return redirect(session.url)
    
    return render(request, 'cancel.html')


def success(request):
    user = request.user
    subscription = Subscription.objects.filter(user=user).order_by('-datetime').first()
    return render(request, "success.html", {"subscription": subscription})

def cancel(request):
    return render(request, "cancel.html")

def error(request):
    return render(request, "error.html")

def orders(request):
    orders = Subscription.objects.filter(user=request.user).order_by('-datetime')
    return render(request, "order.html", {'orders': orders})

def land(request):
    return render(request, "landing.html")

def profile(request):
    user= request.user
    return render(request, "account.html", {'user': user})

@login_required(login_url="/login/")
def home(request):
    return render(request, "home.html")

def authView(request):
    if request.method== "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("base:home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form" :form})

def loginu(request):
    if request.method== "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("base:home")
    else:
       form = AuthenticationForm()
    return render(request, "registration/login.html", {"form" :form})

def logout_view(request):
    logout(request)
    return redirect('/')

def delete_account(request):
    user = request.user
    user.delete()
    return redirect('/')

def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = UpdateProfileForm(instance=user)

    return render(request, 'update_profile.html', {'form': form})