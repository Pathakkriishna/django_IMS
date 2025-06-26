from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from .models import ProductType,Product
from .serializers import ProductTypeSerializer,ProductSerializer
from rest_framework.response import Response
# Create your views here.

class ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductApiView(GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)


