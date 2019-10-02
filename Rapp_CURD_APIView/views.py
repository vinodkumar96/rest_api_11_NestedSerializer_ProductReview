from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product,Review
from .serializers import ProductSerializer,ReviewSerializer
from .permissions import ProductPermission,ReviewPermission

# Create your views here.
class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (ProductPermission)

class ReviewView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,ReviewPermission)
