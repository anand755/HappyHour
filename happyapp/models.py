from django.db import models


# Create your models here.

class Product:
    id: int
    name: str
    description: str
    image: str
    rating: int
    mrp: int
    rate: int
