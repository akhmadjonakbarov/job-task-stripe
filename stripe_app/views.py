
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import stripe
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def get_all_items(request):
    items = Item.objects.all()
    return render(request, 'all_items.html', {'items': items})


def get_stripe_session(request, item_id):
    item = Item.objects.get(pk=item_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),  # Convert to cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )

    return JsonResponse({'session_id': session.id})

def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'item_detail.html', {'item': item})


def success_view(request):
    return render(request, 'success.html')

def cancel_view(request):
    return render(request, 'cancel.html')