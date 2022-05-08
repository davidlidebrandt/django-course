from ast import List, Tuple
from itertools import product
from typing import Any
from django.contrib import admin, messages
from django.http import HttpRequest
from django.db.models.aggregates import Count
from . import models

class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    fields = ['title']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).annotate(
            products_count= Count('product')
        )

class InventoryFilter(admin.SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'inventory'

    def lookups(self, request: Any, model_admin: Any):
        return [
            ('<10', 'Warning')
        ]
    
    def queryset(self, request: Any, queryset):
        if self.value == '<10':
            return queryset.filter(inventory__lt=10)

class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    actions = ['clear_inventory']
    list_display = ['title', 'price', 'quantity_status', 'collection']
    list_editable = ['price']
    list_per_page = 10
    fields = ['title', 'description', 'price', 'inventory', 'collection']
    list_select_related = ['collection']
    list_filter = ['collection', InventoryFilter]
    search_fields = ['title']

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        num_of_products = queryset.update(inventory=0)
        self.message_user(
            request,
            f'Inventory was cleared for {num_of_products} products',
            messages.SUCCESS
        )

    @admin.display(ordering='inventory')
    def quantity_status(self, product):
        if product.inventory < 10:
            return 'Warning'
        return 'OK'

class CustomerAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'phone', 'email', 'birth_date', 'membership']

class AddressAdmin(admin.ModelAdmin):
    fields = ['customer', 'street', 'city']

class FavoriteItemAdmin(admin.ModelAdmin):
    fields = ['customer', 'item_name']

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    fields = ['order', 'product', 'quantity', 'unit_price']
class OrderAdmin(admin.ModelAdmin):
    fields = ['customer', 'payment_status']
    inlines = [OrderItemInline]
class CartAdmin(admin.ModelAdmin):
    fields = ['created_at']

class CartitemAdmin(admin.ModelAdmin):
    fields = ['product', 'cart', 'quantity']

admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.FavoriteItem, FavoriteItemAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartItem, CartitemAdmin)