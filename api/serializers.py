from rest_framework import serializers
from storeapp.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "category", "slug", "inventory", "old_price", "price"]