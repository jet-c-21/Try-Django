"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/18/21
"""
# coding: utf-8
from django.urls import path
from products.views import (product_detail_view,
                            product_create_view,
                            product_delete_view,
                            product_list_view,
                            product_update_view)

'''
As we are make url.py in the app directory so we can remove the root of path
urlpatterns = [
    path('products/', product_list_view, name='product-list'),
    path('products/create/', product_create_view, name='product-list'),
    path('products/<int:product_id>/', product_detail_view, name='product-detail'),
    path('products/<int:product_id>/update/', product_update_view, name='product-update'),
    path('products/<int:product_id>/delete/', product_delete_view, name='product-delete'),
]

'products/<int:product_id>/' -> '<int:product_id>/'
'''

app_name = 'products'

urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-list'),
    path('<int:product_id>/', product_detail_view, name='product-detail'),
    path('<int:product_id>/update/', product_update_view, name='product-update'),
    path('<int:product_id>/delete/', product_delete_view, name='product-delete'),
]
