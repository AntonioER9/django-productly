from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the products index.")
    products = Product.objects.all()
    # products = Product.objects.filter(is_active=True)
    # return HttpResponse(products)
    return JsonResponse(list(products.values()), safe=False)
