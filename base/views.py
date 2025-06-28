from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import ProductType, Product, Purchase, Vendor, Sell, Customer, Department
from .serializers import ProductTypeSerializer, ProductSerializer, PurchaseSerializer, VendorSerializer, SellSerializer, CustomerSerializer, DepartmentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# ----------- Product type  API views -----------
class ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

# ----------- Product API views -----------
class ProductApiView(GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):

        # try:
        #     queryset = Product.objects.get(id=pk)
        # except:
        #     return Response({'error':'Product not found'},status=status.HTTP_404_NOT_FOUND)

        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ----------- Purchse API view -----------
class PurchaseApiView(GenericViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset , many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------- Vendor API view -----------
class VendorApiView(GenericViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ----------- Sells API view -----------
class SellApiView(GenericViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, data=request.data)
        if serializer.is_valid():    
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ----------- Customer API view -----------
class CustomerApiView(GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ----------- Department API view -----------
class DepartmentApiView(GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer 

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

