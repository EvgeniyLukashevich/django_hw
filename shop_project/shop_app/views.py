from django.shortcuts import render
from .models import Customer, Product, Order, OrderItem
from django.utils import timezone


def index(request):
    return render(request, 'shop_app/index.html')


def show_customers(request):
    customers_list = Customer.objects.all()
    return render(request, 'shop_app/homework3.html', {'customers': customers_list})


def week_orders(request, customer_id):
    now = timezone.now()
    one_week_ago = now - timezone.timedelta(days=7)
    orders = Order.objects.filter(date_ordered__gte=one_week_ago, client=customer_id)
    return render(request, 'shop_app/customer_orders.html', {'orders': orders})


def month_orders(request, customer_id):
    now = timezone.now()
    one_month_ago = now - timezone.timedelta(days=30)
    orders = Order.objects.filter(date_ordered__gte=one_month_ago, client=customer_id)
    return render(request, 'shop_app/customer_orders.html', {'orders': orders})

def year_orders(request, customer_id):
    now = timezone.now()
    one_year_ago = now - timezone.timedelta(days=365)
    orders = Order.objects.filter(date_ordered__gte=one_year_ago, client=customer_id)
    return render(request, 'shop_app/customer_orders.html', {'orders': orders})