from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    age = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, upload_to='', default='default.png')


class Order(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        order_details = []
        order_details.append(f"Покупатель: {self.client.name}")
        order_details.append("Товары:")
        for product in self.products.all():
            order_details.append(f"- {product.name} - Цена: {product.price}")
        order_details.append(f"Итоговая сумма: {self.total_price}")
        return "\n".join(order_details)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
