from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, User
from .serializers import ProductSerializer
import random

# Create your views here.


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  ##/api/products/<str:in>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):  ##/api/products/<str:in>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
 
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()

        if not users:
            return Response({'error': 'No users found'}, status=404)

        user = random.choice(users)

        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })