from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homework3/', views.show_customers, name='homework3'),
    path('week_orders/<int:customer_id>/', views.week_orders, name='week_orders'),
    path('month_orders/<int:customer_id>/', views.month_orders, name='month_orders'),
    path('year_orders/<int:customer_id>/', views.year_orders, name='year_orders'),
]
