
from django.urls import path
from .views import get_stripe_session, item_detail, get_all_items, success_view, cancel_view

urlpatterns = [
    path('buy/<int:item_id>/', get_stripe_session, name='get_stripe_session'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
     path('', get_all_items, name='get_all_items'),  
      path('success/', success_view, name='success'),  # Add your success view
    path('cancel/', cancel_view, name='cancel'),
]
