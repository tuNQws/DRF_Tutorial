from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, CategorySerializer
from storeapp.models import Product, Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class ApiProducts(ListCreateAPIView):    
    queryset = products = Product.objects.all()
    serializer_class = ProductSerializer

class ApiProduct(RetrieveUpdateDestroyAPIView):
    queryset = products = Product.objects.all()
    serializer_class = ProductSerializer
    

class ApiCategories(ListCreateAPIView):
    queryset = categories = Category.objects.all()
    serializer_class = CategorySerializer
    # def get(self, request):
    #     categories = Category.objects.all()
    #     serializer = CategorySerializer(categories, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


class ApiCategory(RetrieveUpdateDestroyAPIView):
    queryset = categories = Category.objects.all()
    serializer_class = CategorySerializer
    # def get(self, request, pk):
    #     category = get_object_or_404(Category, category_id=pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data)
    
    # def put(self, request, pk):
    #     category = get_object_or_404(Category, category_id=pk)
    #     serializer = CategorySerializer(category, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    
    # def delete(self, request, pk):
    #     category = get_object_or_404(Category, category_id=pk)
    #     category.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    