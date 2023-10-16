from django.shortcuts import render
from .models import Customer, Product, Order, OrderItem
from .forms import ImageForm
from django.utils import timezone
from django.core.files.storage import FileSystemStorage


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


def show_products(request):
    products_list = Product.objects.all()
    return render(request, 'shop_app/homework4.html', {'products': products_list})


def add_image(request, product_id):
    product = Order.objects.filter(pk=product_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product.objects.filter(pk=product_id).first()
            product.img = image.name
            product.save()
    else:
        form = ImageForm()
    return render(request, 'shop_app/add_image_form.html', {'form': form})
