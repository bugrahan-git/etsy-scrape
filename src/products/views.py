from django.shortcuts import render, get_object_or_404
from products.models import Product
from scrape.views import search

def product_view(req, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product,
    }

    query = req.GET.get('search')
    if query is not None:
        return search(req, context, query)

    return render(req, 'product.html', context)

def products_view(req):
    products = Product.objects.all()
    context = {
        'products': products
    }

    query = req.GET.get('search')
    if query is not None:
        return search(req, context, query)

    return render(req, 'products.html', context)
