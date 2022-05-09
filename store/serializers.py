from rest_framework import serializers
from . models import Collection, Product

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


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