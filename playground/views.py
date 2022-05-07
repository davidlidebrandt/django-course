import collections
from django.shortcuts import render
from django.db.models import Q
from store.models import Product, OrderItem


def hello_world(request):
    product = Product.objects.get(pk=1)
    query_set = Product.objects.all().filter(price__lt=20)
    query_set2 = Product.objects.filter(collection__title="Toys")
    query_set3 = Product.objects.filter(Q(price__lt=20) | Q(title="Hammer")).order_by('title')[1:2]
    query_set4 = Product.objects.values('title', 'price', 'collection__title')
    query_set5 = Product.objects.filter(id__in=OrderItem.objects.values('product__id').distinct())
    query_set6 = Product.objects.select_related('collection').all() # When single related instance
    query_set6 = Product.objects.prefetch_related('promotion').all() # When multiple related instances
    for product in query_set6:
        print(product, product.collection.title)
    return render(request, 'hello.html')
