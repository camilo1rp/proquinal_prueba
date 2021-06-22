from django.urls import  path
from . import views

app_name = 'core'

urlpatterns = [
    path('store-list/', views.StoreList.as_view(), name='store-list'),
    path('product-list/', views.ProductList.as_view(), name='product-list'),
]