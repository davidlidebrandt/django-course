import collections
from decimal import Decimal
from math import prod
from sys import set_asyncgen_hooks
from django.shortcuts import render
from django.db import transaction
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min
from store.models import Collection, Customer, Order, Product, OrderItem


def hello_world(request):
    # product = Product.objects.get(pk=1)
    # query_set = Product.objects.all().filter(price__lt=20)
    # query_set2 = Product.objects.filter(collection__title="Toys")
    # query_set3 = Product.objects.filter(Q(price__lt=20) | Q(title="Hammer")).order_by('title')[1:2]
    # query_set4 = Product.objects.values('title', 'price', 'collection__title')
    # query_set5 = Product.objects.filter(id__in=OrderItem.objects.values('product__id').distinct())
    # query_set6 = Product.objects.select_related('collection').all() # When single related instance
    # query_set6 = Order.objects.prefetch_related('orderitem_set').get(pk=2) # When multiple related instances
    # print(query_set6.orderitem_set.all())
    # #print(Product.objects.aggregate(Count('id')))
    # query_set7 = Product.objects.annotate(price_for_customer=F('price')* Decimal(0.75))
    # for i in query_set7:
    #     print(i.price_for_customer)
    # query_set8 = OrderItem.objects.prefetch_related('product').filter(Q(order__customer__first_name="Joe") & Q(order__customer__last_name='Smith')).distinct()
    # for i in query_set8:
    #     print(i, 'order item')

    # product = Product()
    # product.title = 'Screwdriver'
    # product.description = 'A really good screwdriver'
    # product.price = 12.0
    # product.inventory = 5
    # product.collection = Collection(pk=2)
    # product.save()

    # product = Product.objects.get(pk=1)
    # product.title = 'Hammer'
    # product.save()

    # Product.objects.filter(title='Screwdriver').delete()
    
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     orderitem = OrderItem()
    #     orderitem.order = order
    #     orderitem.product_id = 2
    #     orderitem.quantity = 2
    #     orderitem.unit_price = 12
    #     orderitem.save()

    set = Product.objects.raw('SELECT * FROM store_product')
    for p in set:
        print(p)
    
    return render(request, 'hello.html')
