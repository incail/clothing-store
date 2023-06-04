from django.urls import path

from .views import (CancelTemplateView, OrderCreateView, OrderDetailView,
                    OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-cancled/', CancelTemplateView.as_view(), name='order_cancled'),
    path('', OrderListView.as_view(), name='order'),
    path('detail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
]
