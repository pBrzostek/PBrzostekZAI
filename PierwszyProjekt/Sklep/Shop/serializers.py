from rest_framework import serializers
from .models import ShopCategory, Product

class ShopCategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='product-detail')
    class Meta:
        model = ShopCategory
        fields = ['url', 'name', 'products']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    shop_category = serializers.SlugRelatedField(queryset=ShopCategory.objects.all(), slug_field='name')
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields =['id', 'url', 'NameOfProduct', 'Production_Date', 'Manufacturer', 'Price', 'shop_category', 'owner', ]