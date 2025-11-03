from django.http import HttpResponse

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    
  return render(request,"home.html")

def about(request):
      return render(request,"about.html")


    
def category(request):
   
  return render(request,"category.html")


def product(request):
    products = [
        {"id": 1, "name": "Classic Sneakers", "price": 59.99},
        {"id": 2, "name": "Watch", "price": 40.99},
        {"id": 3, "name": "Jackets", "price": 60.99},
        {"id": 4, "name": "Electronics", "price": 30.99}
    ]
    return render(request, "product.html", {"products": products})
