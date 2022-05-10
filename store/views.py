from os import stat
import re
from unittest import result
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models.aggregates import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . models import Collection, Product
from . serializers import CollectionSerializer, ProductSerializer
from store import serializers

class ProductsList(APIView):
    def get(self, request):
        query_set = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'POST'])
# def products(request):
#     if request.method == 'GET':
#         query_set = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(query_set, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         # if serializer.is_valid():
#         #     serializer.validated_data
#         #     return Response("Success, valid data")
#         # else:
#         #     return Response(status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data) 
    
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitem_set.count() > 0:
            return Response({"error": "Product is present in orders, cannot be deleted"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def product(request, id):
#     product = get_object_or_404(Product, pk=id)
#     if request.method == 'GET':             
#         serializer = ProductSerializer(product)
#         return Response(serializer.data) 
#     elif request.method == 'PUT': 
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE': 
#         if product.orderitem_set.count() > 0:
#             return Response({"error": "Product is present in orders, cannot be deleted"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def collections(request):
    queryset = Collection.objects.annotate(number_of_products=Count('product'))
    if request.method == 'GET':
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
def collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    if request.method == 'GET':             
        serializer = CollectionSerializer(collection)
        return Response(serializer.data) 
    elif request.method == 'PUT': 
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE': 
        if collection.product_set.count() > 0:
            return Response({"error": "Product is present in collection, cannot be deleted"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


