from django.urls import path
from . import views

urlpatterns = [
    path("products", views.api_products),
    path("product/<str:pk>", views.api_product),
    path("categories", views.api_categories),
    path("category/<str:pk>", views.api_category),
]