"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('articles/', include('articles.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, about_view, contact_view

from products.views import (product_detail_view,
                            product_create_view,
                            render_initial_data,
                            dynamic_lookup_view,
                            product_delete_view,
                            product_list_view,
                            product_update_view)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Function views
    path('', home_view, name='home'),
    path('about/', about_view),
    path('contact/', contact_view),
    path('products/', product_list_view, name='product-list'),
    path('products/<int:product_id>/', dynamic_lookup_view, name='product-detail'),
    path('products/<int:product_id>/update/', product_update_view, name='product-update'),
    path('products/<int:product_id>/delete/', product_delete_view, name='product-delete'),
    path('create/', product_create_view),
    path('initial/', render_initial_data),
]
