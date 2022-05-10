from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('products/<int:id>/', views.ProductDetail.as_view()),
    path('collections/', views.collections),
    path('collections/<int:pk>/', views.collection, name='collection'),
]