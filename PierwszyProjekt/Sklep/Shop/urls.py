from django.urls import path
from . import views

urlpatterns = [
    path('shop-categories', views.ShopCategoryList.as_view(), name =views.ShopCategoryList.view_name),
    path('shop-categories/<int:pk>', views.ShopCategoryDetail.as_view(), name =views.ShopCategoryDetail.view_name),
    path('product-list', views.ProductList.as_view(), name=views.ProductList.view_name),
    path('product-list/<int:pk>', views.ProductDetail.as_view(), name=views.ProductDetail.view_name),
    path('',views.ApiRoot.as_view(), name=views.ApiRoot.view_name),
]