from django.contrib import admin
from . import models

class CollectionAdmin(admin.ModelAdmin):
    fields = ['title']

class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'inventory', 'collection']

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