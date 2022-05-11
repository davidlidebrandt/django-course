from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from uuid import uuid4

class Collection(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.title}"

class Product(models.Model):
    class Meta:
        ordering = ['title']       # orders the products on the admin site

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=3, validators=[MinValueValidator(1)])
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title}"

class Customer(models.Model):
    MEMBERSHIP_CHOICES = [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES)

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Address(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}, {self.street}"

class FavoriteItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.item_name}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, models.PROTECT)
    PAYMENT_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_CHOICES[0][0])

    class Meta:
        permissions = [
            ('cancel_order', 'Can cancel order')
        ]

    def __str__(self):
        return f"{self.placed_at}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.product}"

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [['cart', 'product']]

    def __str__(self):
        return f"{self.product}"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

