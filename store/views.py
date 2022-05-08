from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Product
from . serializers import ProductSerializer

@api_view()
def products(request):
    query_set = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(query_set, many=True, context={'request': request})
    return Response(serializer.data)

@api_view()
def product(request, id):
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def collection(request, pk):
    return Response(pk)


