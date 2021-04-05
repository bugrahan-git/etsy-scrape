from django.urls import path
from products.views import product_view

urlpatterns = [
    path('<int:id>/', product_view, name='product'),
]