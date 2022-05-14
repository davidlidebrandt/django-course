from dataclasses import fields
from rest_framework import serializers
from . models import Collection, Order, OrderItem, Product, Review
from djoser.serializers import UserSerializer as BaseUserSerializer

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CollectionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=255)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'number_of_products']
    
    number_of_products = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'inventory', 'collection']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, source='price')
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    # collection_name = serializers.StringRelatedField(source='collection')
    # collection = CollectionSerializer()
    #collection = serializers.HyperlinkedRelatedField(queryset= Collection.objects.all(), view_name='collection')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'description', 'date']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'unit_price']

class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'customer', 'orderitem_set']