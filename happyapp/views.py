from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    product1 = Product()
    product1.id = 1
    product1.name = 'ESSE GOLD'
    product1.description = 'Cigarette comes and goes but gold remains'
    product1.rating = 1
    product1.mrp = 200
    product1.rate = 150
    product1.image = 'categori/product1.png'

    product2 = Product()
    product2.id = 1
    product2.name = 'GOLD Flake'
    product2.description = 'This is gold flake description'
    product2.rating = 2
    product2.mrp = 300
    product2.rate = 250
    product2.image = 'categori/product2.png'

    product3 = Product()
    product3.id = 1
    product3.name = 'Players'
    product3.description = 'Players the real cigerrate'
    product3.rating = 3
    product3.mrp = 100
    product3.rate = 150
    product3.image = 'categori/product3.png'

    product4 = Product()
    product4.id = 1
    product4.name = 'Melbourne'
    product4.description = 'Melbourne a great choice'
    product4.rating = 4
    product4.mrp = 300
    product4.rate = 250
    product4.image = 'categori/product3.png'

    products = [product1, product2, product3, product4]
    return render(request, "index.html", {'products': products})


def category(request):
    return render(request, "category.html")


def product_list(request):
    return render(request, "product_list.html")


def single_product(request):
    return render(request, "single_product.html")


def blog(request):
    return render(request, "blog.html")


def single_blog(request):
    return render(request, "single_blog.html")


def login(request):
    return render(request, "login.html")


def cart(request):
    return render(request, "cart.html")


def elements(request):
    return render(request, "elements.html")


def about(request):
    return render(request, "about.html")


def confirmation(request):
    return render(request, "confirmation.html")


def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")
