"""
URL configuration for IMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import ProductTypeApiView, ProductApiView, PurchaseApiView, GroupApiView, VendorApiView, SellApiView, CustomerApiView, DepartmentApiView, UserApiView

urlpatterns = [
    path('admin/', admin.site.urls),

    # ----------- Product type urls -----------

    path('product/types/',
         ProductTypeApiView.as_view({'get': 'list', 'post': 'create'})),
    path('product/types/<int:pk>/', ProductTypeApiView.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),

    # ----------- Product urls -----------

    path('products/',
         ProductApiView.as_view({'get': 'list', 'post': 'create'})),
    path('products/<int:pk>/',
         ProductApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # ----------- Purchase urls -----------

    path('purchases/',
         PurchaseApiView.as_view({'get': 'list', 'post': 'create'})),
    path('purchases/<int:pk>/', PurchaseApiView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # ----------- Vendor urls -----------

    path('vendors/', VendorApiView.as_view({'get': 'list', 'post': 'create'})),
    path('vendors/<int:pk>/',
         VendorApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # ----------- Sells urls -----------

    path('sells/', SellApiView.as_view({'get': 'list', 'post': 'create'})),
    path('sells/<int:pk>/',
         SellApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # ----------- Customer urls -----------

    path('customers/',
         CustomerApiView.as_view({'get': 'list', 'post': 'create'})),
    path('customers/<int:pk>/', CustomerApiView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # ----------- Department urls -----------

    path('departments/',
         DepartmentApiView.as_view({'get': 'list', 'post': 'create'})),
    path('departments/<int:pk>/', DepartmentApiView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # ------------ User urls -----------
    path('users/register/', UserApiView.as_view({'post': 'register'})),
    path('users/login/', UserApiView.as_view({'post': 'login'})),

    path('groups/', GroupApiView.as_view({'get': 'list'})),
    # path('groups/<int:pk>/',GroupApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),



]
