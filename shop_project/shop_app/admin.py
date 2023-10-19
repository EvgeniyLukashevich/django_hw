from django.contrib import admin
from django.db import models
from .models import Customer, Product, Order, OrderItem


@admin.action(description='Прибавить один год')
def add_year(modeladmin, request, querryset):
    querryset.update(age=models.F('age') + 1)


@admin.action(description='Обнулить запас')
def reset_stock(modeladmin, request, querryset):
    querryset.update(stock=0)


@admin.action(description='Увеличить запас на 1 единицу')
def add_item_to_stock(modeladmin, request, querryset):
    querryset.update(stock=models.F('stock') + 1)


@admin.action(description='Уменьшить запас на 1 единицу')
def reduce_stock_by_one_piece(modeladmin, request, querryset):
    querryset.update(stock=models.F('stock') - 1)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age']
    ordering = ['name']
    list_filter = ['age']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'
    actions = [add_year]
    fields = ['name', 'email', 'age']
    readonly_fields = ['name', 'age']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'stock', 'price', 'img', 'date_added']
    ordering = ['stock']
    list_filter = ['price', 'stock', 'date_added']
    search_fields = ['name']
    search_help_text = 'Поиск по имени товара'
    actions = [reset_stock, add_item_to_stock, reduce_stock_by_one_piece]
    readonly_fields = ['name', 'stock', 'price', 'date_added']
    fieldsets = [
        (
            'GENERAL INFO',
            {
                'classes': ['wide', ],
                'fields': ['name', 'description', 'img', ],
            },
        ),
        (
            'ACCOUNTING',
            {
                'fields': ['stock', 'price', ],
            },
        ),
        (
            'OTHER INFO',
            {
                'classes': ['collapse', ],
                'fields': ['date_added', ],
            },
        ),
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_price', 'date_ordered']
    ordering = ['date_ordered']
    list_filter = ['total_price', 'client', 'date_ordered']
    search_fields = ['client']
    search_help_text = 'Поиск заказа по имени покупателя'
    actions = []
    readonly_fields = ['client', 'total_price', 'date_ordered']
    fieldsets = [
        (
            'GENERAL INFO',
            {
                'classes': ['wide', ],
                'fields': ['client', 'date_ordered', ],
            },
        ),
        (
            'ACCOUNTING',
            {
                'fields': ['total_price', ],
            },
        ),

    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
