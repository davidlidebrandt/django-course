import collections
from django.shortcuts import render
from django.db.models import Q
from store.models import Product


def hello_world(request):
    product = Product.objects.get(pk=1)
    query_set = Product.objects.all().filter(price__lt=20)
    query_set2 = Product.objects.filter(collection__title="Toys")
    query_set3 = Product.objects.filter(Q(price__lt=20) | Q(title="Hammer")).order_by('title')[1:2]
    for product in query_set3:
        print(product)
    return render(request, 'hello.html')
