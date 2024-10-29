from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from storeapp.models import Product
from rest_framework.response import Response

# Create your views here.

@api_view()
def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)