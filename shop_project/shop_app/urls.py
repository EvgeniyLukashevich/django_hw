from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homework3/', views.show_customers, name='homework3'),
    path('orders/<int:customer_id>/', views.week_orders, name='week_order')
]
