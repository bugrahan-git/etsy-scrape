from django.shortcuts import render, get_object_or_404
from scrape.scrape import scrape_url
from products.models import Product

# index
def home_view(req):
    context = {
        'status_message': "",
        'product': None,
    }
    
    if req.method == 'POST':
        url = req.POST.get('etsy_url')
        if url is not None:
            try:
                scraped = scrape_url(url)
                Product.objects.create(name=scraped["name"], image=scraped["image"], price=scraped["price"], url=scraped["url"])
                context['status_message'] = "A product has been added to the database."
            except Exception as e:
                context['status_message'] = e
    elif req.method == 'GET':
        query = req.GET.get('search')
        if query is not None:
            return search(req, context, query)

    return render(req, 'home.html', context)


# Navbar search function
def search(req, context, query):
    context['searched'] = query
    try:
        context['product'] = get_object_or_404(Product, id=query)
        return render(req, 'product.html', context)
    except Exception as e:
        context['status_message'] = e
        return render(req, 'home.html', context)