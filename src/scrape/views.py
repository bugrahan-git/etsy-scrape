from django.shortcuts import render


# index
def home_view(req):
    context = {

    }
    
    return render(req, 'home.html', context)


# Navbar search function
def search(req):
    return None