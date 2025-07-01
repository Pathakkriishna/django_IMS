from rest_framework import serializers
from .models import ProductType,Product,Purchase, Vendor, Sell, Customer, Department
from django.contrib.auth.models import User, Group

from django.contrib.auth.hashers import make_password

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password','groups']

    def create(self, validated_data):
        password = validated_data.get('password')
        hash_password = make_password(password)
        validated_data['password'] = hash_password
        groups = validated_data.pop('groups')

        user = User.objects.create(**validated_data)
        user.groups.set(groups)
        user.save()
        return user
        
        

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']






