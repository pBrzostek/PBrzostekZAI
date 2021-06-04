from .models import ShopCategory, Product
from .serializers import ShopCategorySerializer, ProductSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import FilterSet, DateFilter
from rest_framework import permissions
from .custompermission import IsOwnerOrReadOnly

class ShopCategoryList(generics.ListCreateAPIView):
    queryset = ShopCategory.objects.all()
    serializer_class = ShopCategorySerializer
    view_name = 'shopcategory-list'
    filterset_fields = ['name']
    ordering_fields = ['name']
    search_field = ['name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ShopCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopCategory.objects.all()
    serializer_class = ShopCategorySerializer
    view_name = 'shopcategory-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductFilter(FilterSet):
    min_date = DateFilter(fieldname='Production_Date', lookup_expr='gte')
    max_date = DateFilter(fieldname='Production_Date', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['min_date', 'max_date']

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    view_name = 'product-list'
    filterset_fields = ['NameOfProduct']
    search_field = ['NameOfProduct']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    view_name = 'product-detail'
    permission_classes = [IsOwnerOrReadOnly]

class ApiRoot(generics.GenericAPIView):
    view_name = 'api-view'
    def get(self, request, *args, **kwargs):
        return Response({
            'shop-categories': reverse(ShopCategoryList.view_name,request=request),
            'products': reverse(ProductList.view_name, request=request)
        })