from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("index.html", views.index, name="index"),
               path("category.html", views.category, name="category"),
               path("product_list.html", views.product_list, name="product_list"),
               path("single_product.html", views.single_product, name="single_product"),
               path("blog.html", views.blog, name="blog"),
               path("single_blog.html", views.single_blog, name="single_blog"),
               path("login.html", views.login, name="login"),
               path("cart.html", views.cart, name="cart"),
               path("elements.html", views.elements, name="elements"),
               path("about.html", views.about, name="about"),
               path("confirmation.html", views.confirmation, name="confirmation"),
               path("checkout.html", views.checkout, name="checkout"),
               path("contact.html", views.contact, name="contact")]
