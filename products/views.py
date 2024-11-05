from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()

    return render(request, "index.html", {"products": products})


def detalle(request, producto_id):
    product = get_object_or_404(Product, id=producto_id)

    return render(request, "detalle.html", {"product": product})
